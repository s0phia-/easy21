# file to run for easy21 
from agents.monteCarlo import MonteCarlo
from agents.sarsa import Sarsa
from agents.linearFunctionApprox import FunctionApprox
from utils import mse


if __name__ == "__main__":
    #Q_star = MonteCarlo(no_episodes = 1000000).learn()
    p = np.zeros(11)
    i = 0
    for lmbda in np.arange(0,1.1, 0.1):
        x = Sarsa(episodes = 1000 , lmbda = lmbda)
        q = x.learn()
        
        p[i] = mse(q, Q_star)
        i += 1
    print(p)
        
