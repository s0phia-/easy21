import numpy as np
import random 
from environment import state_space, actions, Easy21, terminal, player_range, dealer_range
from utils import fa_ep_greedy, expand_coarse_code

coarse_code = {'player' : ((1,6), (4,9), (7,12), (10,15), (13,18), (16,21)),\
               'dealer' : ((1,4),(4,7), (7,10)),\
               'action' : (0, 1)}
epsilon = 0.05

class FunctionApprox:
    def __init__(self, lmbda, env = Easy21, coarse_code = coarse_code, max_steps = 100,\
                 no_episodes = 10000, actions = actions, state_space = state_space,
                 gamma = 1, epsilon = epsilon):
        self.env = env
        self.coarse_code = coarse_code
        self.weight_length = np.prod([len(coarse_code[k]) for k in coarse_code.keys()])
        self.episodes = no_episodes
        self.actions = actions
        self.max_steps = max_steps
        self.lmbda = lmbda
        self.state_space = state_space
        self.gamma = gamma
        self.epsilon = epsilon
        
    def phi(self, state, action):
        coarse = self.coarse_code
        curr_player, curr_dealer = state
        curr_action = action
        # create 1 by n array of 0s, where n is the number of dummy vars in the 
        # coarse code
        phi = np.zeros(self.weight_length)
        i = 0
        # set phi[i] to 1 if coarse code satisfied
        for p in range(0, len(coarse['player'])):
            for d in range(0, len(coarse['dealer'])):
                for a in range(0, len(coarse['action'])):
                    (j,k) = coarse['player'][p]
                    if j <= curr_player <= k:
                        (j,k) = coarse['dealer'][d]
                        if j <= curr_dealer <= k:
                    
                            if curr_action == a:
                                phi[i] = 1
                    i += 1
        return phi
    
    def learn(self, alpha = 0.01, terminal = terminal):
        lmbda = self.lmbda
        # initialise weights arbitratily 
        theta = (np.random.rand(self.weight_length) - 0.5)/10
        # loop through episodes
        for _ in range(0, self.episodes):
            # start game
            game = self.env()
            state = game.state
            # first action will be random due to ep greedy
            action = random.choice(self.actions)
            # calculate value of state action pair 
            Q_w = np.dot(self.phi(state, action),theta)
            # to prevent infinite loop
            for _ in range(0, self.max_steps):
                # take action and observe new state and reward
                state_prime, reward = game.step(action)
                # initialise eligibility trace as 0s
                E = np.zeros(self.weight_length)
                if state_prime == terminal:
                    # can update delta with value of Q_prime at that state as 0
                    delta = reward + (lmbda * Q_w)
                else:
                    # select action a′ (using a policy based on Q_w)
                    action_prime = fa_ep_greedy(state_prime, 
                                                weights = theta, 
                                                phi_ftn = self.phi, 
                                                epsilon = self.epsilon)
                    
                    # calculate value of state_prime action_prime pair 
                    Q_w_prime = np.dot(self.phi(state_prime, action_prime),theta)
                    # delta is update of Q, weighted by alpha.
                    # this is gradient descent
                    delta = reward + alpha * (Q_w_prime - Q_w)
                # add current state to eligibility trace
                E += self.phi(state, action)
                # update weights 
                theta += alpha * delta * E   
                # discount eligibility trace by lambda and gamma
                E *= self.lmbda * self.gamma
                if state_prime == terminal:         
                    break
                state, action = state_prime, action_prime
                Q_w = Q_w_prime
        Q = expand_coarse_code(self.coarse_code, p_range = player_range,
                               d_range = dealer_range, a_range = actions,
                               encoding = self.phi, state_space_shape = self.state_space,
                               weights = theta)
        return(Q)
