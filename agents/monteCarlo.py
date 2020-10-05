import numpy as np

from environment import state_space, actions, Easy21, terminal
from utils import ep_greedy

class MonteCarlo:
    def __init__(self, env = Easy21, no_episodes = 10000, N_0 = 100, 
                 max_steps = 100, state_space = state_space):
        self.no_episodes = no_episodes
        self.max_steps = max_steps
        self.N_0 = N_0
        self.state_space = state_space
        self.env = env
        
    def learn(self, state_space = state_space, terminal = terminal):
        N = np.zeros(self.state_space)
        Q = np.zeros(self.state_space)
        visits = np.zeros(self.state_space)
        for episode in range(0, self.no_episodes):
            game = self.env()
            state_actions_visited = []
            for one_step in range(0, self.max_steps):
                state = game.state
                if state == terminal:
                    break
                action = ep_greedy(N, Q, state, self.N_0)
                reward = game.step(action)[1]
                state_actions_visited.append([state, action, reward])
                
            for (player, dealer), action, reward in state_actions_visited:
                index = player-1, dealer-1, action
                N[index] += 1
                alpha = 1/N[index]
                Q[index] += alpha * (reward - Q[index])
                visits[index] += 1
        return Q, visits
            
