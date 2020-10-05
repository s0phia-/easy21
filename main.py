# file to run for easy21 
from agents.monteCarlo import MonteCarlo
from agents.sarsa import Sarsa
from agents.linearFunctionApprox import FunctionApprox
from utils import mse
from visualisations import plot
from environment import player_range, dealer_range

import numpy as np 
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # get Q* by running Monte Carlo with 10m episodes
    Q_star, visits = MonteCarlo(no_episodes = 1000000).learn()
    # plot v* of Q*
    plot(Q_star, player_range,dealer_range)
    for agent in (FunctionApprox, Sarsa):
        # prepare to store MSE of each lambda value
        p = np.zeros((2,11))
        i = 0
        # prepare plot for learning MSE / episode number
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        for lmbda in np.arange(0 ,1.1, 0.1):   
                # initialise class for agent
                x = agent(episodes = 10000 , lmbda = lmbda, 
                                    q_star = Q_star)
                # learn 
                q, error = x.learn()
                # add learning curve to plot for this lambda
                ax1.plot(range(len(error)), error, label = 
                         round(lmbda,1))
                # store MSE and lambda
                p[0,i] = lmbda
                p[1,i] = mse(q, Q_star)
                i += 1       
        # plot learning curve of mse against episode number
        plt.legend(loc='best', title = "Lambda");
        plt.title(f"Learning Method: {agent}")
        plt.show()
            
        # plot MSE against lambda 
        plt.figure()
        plt.plot(p[0], p[1])
        plt.title(f"Learning Method: {agent}")
        plt.figure()
        
        