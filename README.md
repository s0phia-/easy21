# Using Reinforcement Learning (RL) to play Easy21 

Easy21 is a variant of the game blackjack, introduced in the [coursework](https://www.davidsilver.uk/wp-content/uploads/2020/03/Easy21-Johannes.pdf) for the Deepmind X UCL [Reinforcement Learning Course](https://deepmind.com/learning-resources/-introduction-reinforcement-learning-david-silver) run by David Silver. This project provides solutions to all questions in the coursework.

The rules of the game are:

- The game is played with an infinite deck of cards (i.e. cards are sampled
with replacement)
- Each draw from the deck results in a value between 1 and 10 (uniformly
distributed) with a colour of red (probability 1/3) or black (probability
2/3).
- There are no aces or picture (face) cards in this game
- At the start of the game both the player and the dealer draw one black
card (fully observed)
- Each turn the player may either stick or hit
- If the player hits then she draws another card from the deck
- If the player sticks she receives no further cards
- The values of the player’s cards are added (black cards) or subtracted (red
cards)
- If the player’s sum exceeds 21, or becomes less than 1, then she “goes
bust” and loses the game (reward -1)
- If the player sticks then the dealer starts taking turns. The dealer always
sticks on any sum of 17 or greater, and hits otherwise. If the dealer goes
bust, then the player wins; otherwise, the outcome – win (reward +1),
lose (reward -1), or draw (reward 0) – is the player with the largest sum.

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
