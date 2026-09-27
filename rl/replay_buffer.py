from collections import deque
import random

class replaybuffer():
    def __init__(self, capacity=50000):
        self.memory = deque(maxlen=capacity)

    def add_moment(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def select_a_random_moment(self, batch_size):
        if len(self.memory) <= batch_size:
            return random.sample(self.memory, len(self.memory))

        return random.sample(self.memory, batch_size)

    def memory_size(self):
        return len(self.memory)
    