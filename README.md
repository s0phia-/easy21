# Using Reinforcement Learning (RL) to play Easy21 

Easy21 is a variant of the game blackjack, introduced in the [coursework](https://www.davidsilver.uk/wp-content/uploads/2020/03/Easy21-Johannes.pdf) for the Deepmind X UCL [Reinforcement Learning Course](https://deepmind.com/learning-resources/-introduction-reinforcement-learning-david-silver) run by David Silver. This project provides solutions to all questions in the coursework.

## Monte Carlo Control

A Monte Carlo control algorithm is applied to the easy21 game for 10mil episodes to find a good estimation of the true value function of the game. The value function is plotted below, and as one might intuitively guess, states where the player's hand sum is near to 21 tend to have a higher value. 

![Monte Carlo Plot](/plots/Q_star.png)

Perhaps less intuitively, the states where the dealer has a high hand total have the lowest value, even when the player has a much higher hand total. The explanation here lies in the game rules that give cards a negative value with probability 1/3, and the rule that a hand sum below 1 is bust. Thus when the dealer has a low value hand, they have a greater chance of going bust, and therefore ensuring a win for the agent. This risk of going negative has another affect on agent behaviour -- the agent prefers to stick in states with a very low player hand total. The agent sees that the risk of going bust is too high, and prefers to stick and hope that the dealer will go bust instead.

## TD Learning with Sarsa

![Monte Carlo Plot1](/plots/Sarsa_episode_error.png)

![Monte Carlo Plot2](/plots/Sarsalambda_error.png)

## Linear Function Value Approximation

![Monte Carlo Plot3](/plots/FunctionApprox_episode_error.png)

![Monte Carlo Plot4](/plots/FunctionApproxlambda_error.png)
