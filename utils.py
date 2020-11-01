# ep greedy, mse, other random functions 
from environment import actions
import numpy as np
import random

def ep_greedy(Nsa, Qsa, state, N_0, actions = actions):
    player, dealer = state
    Ns = np.sum(Nsa[player-1, dealer-1, :])
    # get epsilon 
    epsilon = N_0/(N_0 + Ns)
    # with probability 1-epsilon, pick action using state action values
    if random.random() > epsilon:
        action = np.argmax(Qsa[player-1, dealer-1, :])
    # with probability epsilon, explore
    else:
        action = random.choice(actions)
    return(action)
    
# version of epsilon greedy to work with function approximators
def fa_ep_greedy(state, weights, phi_ftn, epsilon, actions = actions):
    if random.random() > epsilon:
        # exploit
        action_values = [np.dot(phi_ftn(state, a),weights) for a in actions]
        action = np.argmax(action_values)
    else:
        # explore
        action = np.random.choice(actions)
    return(action)  

def expand_coarse_code(coarse_code, p_range, d_range, a_range, encoding, 
                       state_space_shape, weights):
    Q = np.zeros(state_space_shape)
    for p in p_range:
        for d in d_range:
            for a in a_range:
                #print(a, p , d, sum(encoding((p, d), a)))
                Q[p-1, d - 1, a] += np.dot(encoding((p, d), a),weights)
    return(Q)
    
def mse(X,Y):
    mse = np.sum((X-Y)**2)/np.size(X)
    return(mse)