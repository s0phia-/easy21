import numpy as np
import random 
from environment import state_space, actions, Easy21, terminal
from utils import fa_ep_greedy

coarse_code = {'player' : ((1,6), (4,9), (7,12), (10,15), (13,18), (16,21)),\
               'dealer' : ((1,4),(4,7), (7,10)),\
               'action' : (0,1)}
epsilon = 0.05

class FunctionApprox:
    def __init__(self, env = Easy21, coarse_code = coarse_code, max_steps = 100,\
                 no_episodes = 10000,
                 actions = actions):
        self.env = env
        self.coarse_code = coarse_code
        self.weight_length = np.prod([len(coarse_code[k]) for k in coarse_code.keys()])
        self.episodes = no_episodes
        self.actions = actions
        self.max_steps = max_steps
        
    def phi(self, state, action):
        coarse = self.coarse_code
        player, dealer = state
        # create 1 by n array of 0s, where n is the number of dummy vars in the 
        # coarse code
        phi = np.zeros(len(coarse['player'])+\
                          len(coarse['dealer'])+\
                          len(coarse['action']))
        # set phi i to 1 if coarse code satisfied
        for i in range(0, len(coarse['player'])-1):
            (j,k) = coarse['player'][i]
            if j <= player <= k:
                phi[i] = 1
        for i in range(0, len(coarse['dealer'])-1):
            (j,k) = coarse['dealer'][i]
            if j <= dealer <= k:
                phi[i + len(coarse['player'])] = 1
        for i in range(0, len(coarse['action'])-1):
            if action == i:
                phi[i + len(coarse['player']) + len(coarse['dealer'])] = 1
        return phi
    
    def learn(self):
        # initialise weights arbitratily 
        theta = (np.random.rand(self.weight_length) - 0.5)/10
        # loop through episodes
        for _ in range(0, self.episodes):
            # start game
            game = self.env()
            state = game.state
            player, dealer = state
            # initialise eligibility trace
            E = np.zeros(self.weight_length)
            # first action will be random due to ep greedy
            action = random.choice(self.actions)
            for _ in range(0, self.max_steps):
                # take action and observe new state and reward
                state_prime, reward = game.step(action)
                #player_prime, dealer_prime = state_prime
                
                # here is where things start to get tricky... how do i do ep greedy without Q? I'll 
                # figure it out, I'm a smart gal.
                # select action a′ (using a policy based on Q_w)
                action_prime = fa_ep_greedy(state_prime, 
                                            weights = theta, 
                                            phi_ftn = self.phi, 
                                            epsilon = epsilon)
                print(action_prime)


            


# theta is weights

