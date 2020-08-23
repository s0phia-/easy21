import numpy as np
import random

from environment import state_space, actions, Easy21, terminal
from utils import ep_greedy

class Sarsa:
    def __init__(self, lmbda = 0.5, env = Easy21, max_steps = 100,\
                 episodes = 10000, gamma = 1, N_0 = 100, state_space = state_space):
        self.lmbda = lmbda
        self.env = env
        self.max_steps = max_steps
        self.episodes = episodes
        self.gamma = gamma
        self.N_0 = N_0
        self.state_space = state_space
        
    def learn(self, actions = actions, terminal = terminal):
       N = np.zeros(self.state_space)
       Q = np.zeros(self.state_space)
       for _ in range(0, self.episodes):
           game = self.env()
           state = game.state
           E = np.zeros(self.state_space)
           action = random.choice(actions)
           for _ in range(0, self.max_steps):
               state_prime, reward = game.step(action)
               player, dealer = state
               index = player-1, dealer - 1, action
               N[index] += 1
               if state_prime == terminal:
                   delta = reward + self.lmbda * (-Q[index])
               else:
                   action_prime = ep_greedy(N, Q, state_prime, self.N_0)
                   player_prime, dealer_prime = state_prime
                   index_prime = player_prime - 1, dealer_prime - 1, action_prime
                   delta = reward + self.lmbda * (Q[index_prime] - Q[index])
               E[index] += 1
               alpha = 1/N[index]
               Q += alpha * delta * E
               E *= self.lmbda * self.gamma
               if state_prime == terminal:
                   break
               state, action = state_prime, action_prime
               
       return Q
