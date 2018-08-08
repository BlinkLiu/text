import numpy as np
import random
from collections import defaultdict
from enviroment import Env

class Mc_agent:
    def __init__(self, actions):
        self.width = 5
        self.height = 5
        self.actions = actions
        self.learning_rate = 0.01
        self.discount_factor = 0.9
        self.epsilon = 0.1
        self.samples = []
        self.value_table = defaultdict(float)

    def save_sample(self, state, reward, done):
        self.samples.append([state, reward, done])

#Q-learning 算法更新价值函数Q
    def update(self):
        g_t = 0
        visit_state = []
        for reward in reversed(self.samples):
            state = str(reward[0])
            if state not in visit_state:
                visit_state.append(state)
                g_t = self.discount_factor*(reward[1]+g_t)
                value = self.value_table[state]
                self.value_table[state] = value+self.learning_rate*(g_t-value)

#epsilon greedy 策略，当随机数小于e时，探索，大于e时利用
    def get_action(self, state):
        if np.random.rand() < self.epsilon:
            action = np.random.choice(self.actions)
        else:
            next_state = self.possible_next_state(state)
            action = self.arg_max(next_state)
        return int(action)

#arg_max,如果有多个可选项，则随机选择一个
    @staticmethod
    def arg_max(next_state):
        max_index_list = []
        max_value = next_state[0]
        for index, value in enumerate(next_state):
            if value > max_value:
                max_index_list.clear()
                max_value = value
                max_index_list.append(index)
            elif value == max_value:
                max_index_list.append(index)
        return random.choice(max_index_list)

#给出可能的四个下一步
    def possible_next_state(self, state):
        col, row = state
        next_state = [0.]*4
        if row != 0:
            next_state[0] = self.value_table[str([col,row-1])]
        else:
            next_state[0] = self.value_table[str(state)]
        if row != self.height-1:
            next_state[1] = self.value_table[str([col,row+1])]
        else:
            next_state[1] = self.value_table[str(state)]
        if col != 0:
            next_state[2] = self.value_table[str([col-1,row])]
        else:
            next_state[2] = self.value_table[str(state)]
        if col != self.width-1:
            next_state[3] = self.value_table[str([col+1, row])]
        else:
            next_state[3] = self.value_table[str(state)]

        return next_state


if __name__ == "__main__":
    envp = Env()
    agent = Mc_agent(actions=list(range(envp.n_actions)))
    for episode in range(10000):
        state = envp.reset()
        action = agent.get_action(state)
        while True:
            envp.render()
            next_state, reward, done = envp.step(action)
            agent.save_sample(next_state, reward, done)
            action = agent.get_action(next_state)
            if done:
                print("episode:", episode)
                agent.update()
                agent.samples.clear()
                break
