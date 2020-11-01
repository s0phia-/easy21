# file to run for easy21 
from agents.monteCarlo import MonteCarlo
from agents.sarsa import Sarsa
from agents.linearFunctionApprox import FunctionApprox
from utils import mse
from visualisations import value_plot, prep_ep_error, episode_error_plot, lambda_error_plot
from environment import player_range, dealer_range

import numpy as np 
import pandas as pd

agents = (FunctionApprox, Sarsa)
lambdas = np.arange(0 ,1.1, 0.1)
episode_runs = 10000
plots_path = "plots/"

if __name__ == "__main__":
    # get Q* by running Monte Carlo with 10m episodes
    Q_star, visits = MonteCarlo(no_episodes = 10000000).learn()
    # plot v* of Q*
    value_plot(Q_star, player_range,dealer_range, plots_path, 'Q_star.png')
    
    # initialise list and df to hold MSE values
    save_mse = list()
    episode_error = pd.DataFrame()
    # loop through agents
    for agent in agents:
        # add episode number
        episode_error['episode'] = range(0,episode_runs)
        for lmbda in lambdas:   
            # initialise class for agent
            x = agent(episodes =  episode_runs, lmbda = lmbda, 
                                q_star = Q_star)
            # learn 
            Q, error = x.learn()
            # add a column to the episode_error df for each agent and lambda 
            #combination
            episode_error[agent.__name__ + "," + str(lmbda)] = error
            # store MSE for agent and lambda
            save_mse.append([agent.__name__, lmbda, mse(Q, Q_star)])  
    # convert list of lists to pd.dataframe
    save_mse_df = pd.DataFrame(save_mse, columns = ("agent", "lambda", "mse"))
    save_mse_df['Lambda'] = round(save_mse_df['lambda'].astype('float'),1)
    
    # plots!
    plot_ep_error = prep_ep_error(episode_error)
    
    for agent in agents:
        episode_error_plot(plot_ep_error, agent, plots_path)
        lambda_error_plot(save_mse_df, agent, plots_path)  
  
    
    
    
    
    
    
    
    
    
    