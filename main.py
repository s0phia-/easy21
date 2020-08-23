# file to run for easy21 
#import config
from agents.monteCarlo import MonteCarlo
from agents.sarsa import Sarsa
#import sarsa
#import visualisations 

import numpy as np

if __name__ == "__main__":
    # do stuff
    x = MonteCarlo(no_episodes = 1000000)
    q = x.learn()
    t = [(p+1, d+1, np.argmax(q[p, d, :])) for p in range(0,21) for d in range(0,10)]       
