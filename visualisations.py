#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 19:13:57 2020

@author: sophiajones
"""

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
   
def plot(df,player_range,dealer_range):

    z = df.max(axis = 2)
    x,y = np.mgrid[player_range, dealer_range]

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    #ax.plot_wireframe(y, x, z, color = 'black')
    ax.plot_surface(y, x, z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
    ax.set_xlabel('Dealer Hand')
    ax.set_ylabel('Player Hand')
    ax.set_zlabel('Value *');

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    