from model import qnetwork
from replay_buffer import replaybuffer
import torch
import torch.nn as nn
import torch.optim as optim
import random

class dqnagent():
    def __init__(self, lr=0.001):
        self.policy_net = qnetwork()
        self.target_net = qnetwork()

        # Target net'in ağırlıklarını başlangıçta policy net ile aynı yapıyoruz
        self.target_net.load_state_dict(self.policy_net.state_dict())
        self.target_net.eval() 
        
        # Target net sadece tahmin yapacağı için eval moduna alıyoruz
        self.memory = replaybuffer()
        
        # 2. Optimizer olarak en çok tercih edilen Adam'ı ekledik
        # Sadece policy_net parametrelerini optimize ediyoruz!
        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=lr)

        self.criterion = nn.MSELoss()
        self.epsilon = 1.0

    def choose_action(self, state, last_action=None):
        if random.random() <= self.epsilon:
            if last_action is not None:
                forbidden = last_action ^ 1
                available = [a for a in range(12) if a != forbidden]
                return random.choice(available)
            return random.randint(0, 11)
        state_tensor = torch.tensor(state, dtype=torch.float32).unsqueeze(0)

        with torch.no_grad():
            q_values = self.policy_net(state_tensor)
            if last_action is not None:
                forbidden = last_action ^ 1
                q_values[0, forbidden] = -float('inf')

        action = torch.argmax(q_values, dim=1).item()

        return action

    def learn(self, batch_size=64, gamma=0.9):
        if self.memory.memory_size() < batch_size: return
        batch = self.memory.select_a_random_moment(batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)

        states_t = torch.tensor(states, dtype=torch.float32)
        actions_t = torch.tensor(actions, dtype=torch.int64).unsqueeze(1)
        rewards_t = torch.tensor(rewards, dtype=torch.float32).unsqueeze(1)
        next_states_t = torch.tensor(next_states, dtype=torch.float32)
        dones_t = torch.tensor(dones, dtype=torch.float32).unsqueeze(1)

        current_q_values = self.policy_net(states_t).gather(1, actions_t)
    
        with torch.no_grad():
            next_q_values = self.target_net(next_states_t).max(dim=1, keepdim=True)[0]
            target_q_values = rewards_t + (gamma * next_q_values * (1 - dones_t))
    
        loss = self.criterion(current_q_values, target_q_values)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

    def update_target_network(self):
        self.target_net.load_state_dict(self.policy_net.state_dict())