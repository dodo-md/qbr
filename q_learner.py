import random

class qagent():
    def __init__(self):
        self.action_size = 12
        self.lr = 0.1
        self.gamma = 0.9
        self.epsilon = 1.0
        self.q_table = {}

    def get_q(self, state):
        state_key = tuple(state)

        if state_key not in self.q_table: self.q_table[state_key] = [0.0] * self.action_size
        return self.q_table[state_key]

    def choose_action(self, state):
        zar = random.random()

        if zar <= self.epsilon:
            return random.randint(0, 11)
        else:
            q_values = self.get_q(state)
            return q_values.index(max(q_values))

    def learn(self, state, action, reward, next_state, done):
        current_q = self.get_q(state)[action]

        if done:
            target = reward
        else:
            target = reward + self.gamma * max(self.get_q(next_state))

        new_q = current_q + self.lr * (target - current_q)
        self.q_table[tuple(state)][action] = new_q

if __name__ == "__main__":
    from env import cubeenv
    env = cubeenv()
    agent = qagent()
    episodes = 3000

    for episode in range(episodes):
        state = env.reset(scramble_moves=2)
        done = False
        total_reward = 0
        while not done:
            action = agent.choose_action(state)
            next_state, reward, done, _ = env.step(action)
            total_reward += reward
            agent.learn(state, action, reward, next_state, done)
            state = next_state
        if agent.epsilon > 0.05:
            agent.epsilon *= 0.99
        if episode % 50 == 0: print(f"match: {episode} | points: {total_reward:.1f} | curiosity: {agent.epsilon:.2f} | is it solved: {env.cube.is_solved()}")