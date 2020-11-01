#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 19:13:57 2020

@author: sophiajones
"""

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
   
def value_plot(df,player_range,dealer_range, plots_path, name):
    plt.figure()
    z = df.max(axis = 2)
    x,y = np.mgrid[player_range, dealer_range]

    ax = plt.axes(projection='3d')
    #ax.plot_wireframe(y, x, z, color = 'black')
    ax.plot_surface(y, x, z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
    ax.set_xlabel('Dealer Hand')
    ax.set_ylabel('Player Hand')
    ax.set_zlabel('V*')
    return(ax)
    
def prep_ep_error(data):
    # convert episodic error wide to long
    m_data = pd.melt(data, ['episode'], value_name = "mse",
                              var_name = "lambda")
    # split lambda and agent into separate columns
    m_data[['agent','lambda']] = m_data['lambda'].str.split(',',expand=True)
    # reset lambda as a float
    m_data['Lambda'] = round(m_data['lambda'].astype('float'),1)
    return(m_data)
    
def episode_error_plot(df, learning_agent, save_path):
    plt.figure()
    g = sns.relplot(x="episode", y="mse", hue = "Lambda", kind="line", 
                    legend="full",
                    data=df[df['agent'] == learning_agent.__name__])
    g.set(xlabel='Episode Number', ylabel='Mean Sqared Error (MSE)',
          title = learning_agent.__name__ + ": Mean Squared Error by Episode Number")

    g.savefig(save_path + learning_agent.__name__ + "_episode_error.png")
    return(g)
   
def lambda_error_plot(df, learning_agent, save_path):
    plt.figure()
    g = sns.pointplot(x = "Lambda", y = "mse", ci = None, 
                            data = df[df['agent'] == learning_agent.__name__])
    g.set(xlabel = 'Lambda', ylabel = 'Mean Sqared Error (MSE)',
                  title = learning_agent.__name__ + ": Mean Squared Error by Lambda")
    g.figure.savefig(save_path + learning_agent.__name__ + "lambda_error.png")
    return(g)

    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    