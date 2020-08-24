import numpy as np
import random 
from environment import state_space, actions, Easy21, terminal
from utils import ep_greedy

coarse_code = {'player' : ((1,6), (4,9), (7,12), (10,15), (13,18), (16,21)),\
               'dealer' : ((1,4),(4,7), (7,10)),\
               'action' : (0,1)}



# theta is weights

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
        
    @staticmethod
    def sigma(state, action, coarse = self.coarse_code):
        player, dealer = state
        # create 1 by n array of 0s, where n is the number of dummy vars in the 
        # coarse code
        sigma = np.zeros(len(coarse['player'])+\
                          len(coarse['dealer'])+\
                          len(coarse['action']))
        # set sigma i to 1 if coarse code satisfied
        for i in range(0, len(coarse['player'])-1):
            (j,k) = coarse['player'][i]
            if j <= player <= k:
                sigma[i] = 1
        for i in range(0, len(coarse['dealer'])-1):
            (j,k) = coarse['dealer'][i]
            if j <= dealer <= k:
                sigma[i + len(coarse['player'])] = 1
        for i in range(0, len(coarse['action'])-1):
            if action == i:
                sigma[i + len(coarse['player']) + len(coarse['dealer'])] = 1
        return sigma
    
    def learn(self):
        # initialise weights arbitratily 
        theta = (np.random.rand(self.weight_legnth) - 0.5)/10
        # loop through episodes
        for _ in range(0, self.episodes):
            game = self.env()
            state = game.state
            E = np.zeros(self.weight_length)
            action = random.choice(self.actions)
            for _ in range(0, self.max_steps):
                state_prime, reward = game.step(action)
                player, dealer = state
                # here is where things start to get tricky... how do i do ep greedy without Q? I'll 
                # figure it out, I'm a smart gal.






#We now consider a simple value function approximator using coarse coding. Use
#a binary feature vector 
#(s; a) with 3  6  2 = 36 features. Each binary feature
#has a value of 1 i
# (s; a) lies within the cuboid of state-space corresponding to
#that feature, and the action corresponding to that feature. The cuboids have
#the following overlapping intervals:
#dealer(s) = f[1; 4]; [4; 7]; [7; 10]g
#player(s) = f[1; 6]; [4; 9]; [7; 12]; [10; 15]; [13; 18]; [16; 21]g
#a = fhit; stickg
#where
# dealer(s) is the value of the dealer's 
#rst card (1{10)
# sum(s) is the sum of the player's cards (1{21)
#Repeat the Sarsa() experiment from the previous section, but using linear
#value function approximation Q(s; a) = 
#(s; a)>. Use a constant exploration
#of  = 0:05 and a constant step-size of 0:01. Plot the mean-squared error against
#. For  = 0 and  = 1 only, plot the learning curve of mean-squared error
#against episode number.