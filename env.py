from state import CubeState
import random

class cubeenv():
    def __init__(self):
        self.cube = CubeState()
        self.actions = ["U", "U'", "D", "D'", "R", "R'", "L", "L'", "F", "F'", "B", "B'"]
        self.max_steps = 20
        self.current_step = 0
        pass

    def get_observation(self):
        return self.cube.cp + self.cube.co + self.cube.ep + self.cube.eo

    def reset(self, scramble_moves=1):
        self.cube = CubeState()
        self.current_step = 0
        for _ in range(scramble_moves):
            move = random.choice(self.actions)
            self.cube.apply_move(move)
        return self.get_observation()

    def step(self, action):
        move = self.actions[action]
        self.cube.apply_move(move)
        self.current_step += 1

        if self.cube.is_solved():
            reward = 10.0
            done = True
        else:
            reward = -0.1
            done = self.current_step >= self.max_steps

        obs = self.get_observation()
        return obs, reward, done, {}

if __name__ == "__main__":
    env = cubeenv()
    obs = env.reset(scramble_moves=1)
    done = False
    total_reward = 0

    while not done:
        action = random.randint(0, 11)
        obs, reward, done, _ = env.step(action)
        total_reward += reward
    print(f"total points: {total_reward}")
    print(f"is it solved: {env.cube.is_solved()}")