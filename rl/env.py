from core.state import CubeState
import random

class cubeenv():
    def __init__(self, goal="full"):
        self.cube = CubeState()
        self.actions = ["U", "U'", "D", "D'", "R", "R'", "L", "L'", "F", "F'", "B", "B'"]
        self.max_steps = 30
        self.current_step = 0
        self.goal = goal

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
        old_cross = self.cube.count_cross_edges()
        self.cube.apply_move(move)
        new_cross = self.cube.count_cross_edges()
        self.current_step += 1

        if self.goal == "cross":
            if self.cube.is_cross_solved():
                reward = 10.0
                done = True
            elif new_cross > old_cross:
                reward = 2.0
                done = False
            elif new_cross < old_cross:
                reward = -2.0
                done = False
            else:
                reward = -0.1
                done = self.current_step >= self.max_steps
        else:
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