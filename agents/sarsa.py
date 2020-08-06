from functions import *
from game import *

def sarsa_lambda(max_steps_per_episodes = 100, episodes = 10000, gamma = 1, 
                 actions = ['hit', 'stick'], lbda = 0.5):
        N0 = 100
        Qsa = init_Msa()
        Nsa = init_Msa()
        player_hand = np.arange(1,22,1)
        dealer_hand = np.arange(1,11,1)
        states = tuple(itertools.product(player_hand, dealer_hand)) + ("terminal",)
        for episodes in range(0,episodes):
            Esa = init_Msa()
            state = (start_draw(), start_draw())
            action = random.choice(list(actions))
            #state_actions = set()
            for one_step in range(0,max_steps_per_episodes):
                # update N(S,A)
                update_N(Nsa, state, action)    
                Ns = sum(Nsa.get((state, i)) for i in actions)
                #state_actions.add(tuple([player, dealer, action]))
                # take one step
                state_prime, reward = step(action, state)
                # get epsilon and epsilon greedy action
                epsilon = N0/(N0 + Ns)
                # choose A'
                action_prime = ep_greedy(epsilon, actions, Qsa,
                               state_prime)  
                Q = Qsa.get((state, action))
                Q_prime = Qsa.get((state_prime, action_prime))
                delta = reward + gamma*(Q_prime - Q)
                update_N(Esa, state, action)
                alpha = 1/Nsa.get((state, action))
                for each_state in states:
                    for each_action in actions:
                        Q = Qsa.get((each_state, each_action))
                        E = Esa.get((each_state, each_action))
                        Qsa.update({(each_state, each_action) : Q + alpha * delta * E})
                        Esa.update({(each_state, each_action): gamma * lbda * E})
                state = state_prime 
                action = action_prime
                # if state is terminal, end episode
                if state == "terminal":
                    break
        return(Qsa)

Qsa = sarsa_lambda()              
                