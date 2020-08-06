#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 19:15:08 2020

@author: sophiajones
"""

def q2(max_steps_per_episodes = 100, episodes = 1000000, N_0 = 100,
       actions = ['hit', 'stick']):
    Qsa = init_Msa()
    # initialise N(s,a)
    Nsa = init_Msa()
    # init G
    for episode in range(0, episodes):
        # initialise hands
        state = (start_draw(), start_draw())
        # keep track of state action combination visited in one episode
        state_actions_visited = set()
        # take up to max_steps_per_episodes in an episode before terminating, 
        #to avoid infinite episodes
        for one_step in range(0,max_steps_per_episodes):
            # update N(s)_t
            Ns = sum(Nsa.get((state, i)) for i in actions)
            # get epsilon and epsilon greedy action
            epsilon = N_0/(N_0 + Ns)
            action = ep_greedy(epsilon, actions, Qsa, state)       
            # update N(S,A)
            update_N(Nsa, state, action) 
            state_actions_visited.add((state, action))
            # take one step
            state, reward = step(action, state)
            # check whether state is terminal
            if state == "terminal":
                break
        update_Q(Nsa, Qsa, reward, state_actions_visited)
    return(Qsa)
    

q = q2()      
v = get_V(q)
plot_optimal_value_function(v)


