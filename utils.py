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
    # with probability epsilon, pick randomly
    else:
        action = random.choice(actions)
    return(action)
    
# version of epsilon greedy to work with function approximators
def fa_ep_greedy(state, weights, phi_ftn, epsilon, actions = actions) :
    if np.random.rand() < (1 - epsilon):
        action = np.argmax(phi_ftn(state, a)*weights for a in actions)
    else:
        action = np.random.choice(actions)
    return(action)  
