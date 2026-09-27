from env import cubeenv
from dqn_agent import dqnagent
import random
import torch

env = cubeenv(goal="cross")
agent = dqnagent(lr=0.001)
episodes = 2000

for episode in range(episodes):
    state = env.reset(scramble_moves=random.randint(1, 2))
    done = False
    total_reward = 0
    last_action = None
    while not done:
        action = agent.choose_action(state, last_action)
        next_state, reward, done, _ = env.step(action)
        agent.memory.add_moment(state, action, reward, next_state, done)
        agent.learn(batch_size=64)
        state = next_state
        total_reward += reward
        last_action = action

    if agent.epsilon > 0.05: agent.epsilon *= 0.995
    if episode % 10 == 0: agent.update_target_network()

    if episode % 50 == 0:
        print(f"match: {episode} | points: {total_reward:.1f} | curiosity: {agent.epsilon:.2f} | is cross solved: {env.cube.is_cross_solved()}")

# test ride
agent.epsilon = 0.0
print("\n--- test ride ---")
for i in range(5):
    state = env.reset(scramble_moves=2)
    done = False
    moves = []
    last_action = None
    while not done:
        action = agent.choose_action(state, last_action)
        moves.append(env.actions[action])
        state, reward, done, _ = env.step(action)
        last_action = action
    print(f"test {i+1}: moves={moves} | solved={env.cube.is_cross_solved()}")

torch.save(agent.policy_net.state_dict(), "qbr_dqn.pth")
print("successfully saved")