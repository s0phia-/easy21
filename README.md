# Using Reinforcement Learning (RL) to play Easy21 

Easy21 is a variant of the game blackjack, introduced in the [coursework](https://www.davidsilver.uk/wp-content/uploads/2020/03/Easy21-Johannes.pdf) for the Deepmind X UCL [Reinforcement Learning Course](https://deepmind.com/learning-resources/-introduction-reinforcement-learning-david-silver) run by David Silver. This project provides solutions to all questions in the coursework.

## Monte Carlo Control

A Monte Carlo control algorithm is applied to the easy21 game for 10mil episodes to find a good estimation of the true value function of the game. The value function is plotted below, and as one might intuitively guess, states where the player's hand sum is near to 21 tend to have a higher value. 

![Monte Carlo Plot](/plots/Q_star.png)

Perhaps less intuitively, the states where the player has a lower hand decrease in value as the dealer's hand increases in value. The explanation here lies in the game rules that gives cards a negative value with probability 1/3, and that a hand sum below 1 is bust. Thus when the dealer has a lower value hand, they have a greater chance of going bust - in fact, in these low hand sum states the agent often chooses to stick with a very low value hand rather than risk going bust - and hope that the dealer goes bust instead.



![Monte Carlo Plot1](/plots/Sarsa_episode_error.png)

![Monte Carlo Plot2](/plots/Sarsalambda_error.png)

![Monte Carlo Plot3](/plots/FunctionApprox_episode_error.png)

![Monte Carlo Plot4](/plots/FunctionApproxlambda_error.png)
