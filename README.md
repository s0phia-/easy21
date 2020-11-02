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

Monte Carlo control plays out whole episodes without bootstrapping to obtain a value function. In this example, episodes tend to be short in length. However for games with lengthly episodes Monte Carlo control takes a very long time to learn or may be entirely unsuitable. 

## TD Learning with Sarsa

Sarsa lambda is used to learn the value function, with lambda = 0.0, 0.1,...,1.0. Plots below show the learning curve for each lambda, and the final mean squared error (MSE) after 10,000 iterations for each lambda.

![Sarsa episode](/plots/Sarsa_episode_error.png)

![Sarsa lambda](/plots/Sarsalambda_error.png)

## Linear Function Value Approximation

A linear function approximator is used to estimate the action value function. With previous agents, the state action value is found for every single state. Here, the state space is compressed using coarse coding, so that the value of features, rather than states, is learned. Similar to Sarsa, the plots show the learning curve over 10,000 episodes, and the final MSE for each lambda value.

![LF episode](/plots/FunctionApprox_episode_error.png)

![LF lambda](/plots/FunctionApproxlambda_error.png)

## Discussion Topics

### What are the pros and cons of bootstrapping in Easy21?

#### Pros:
Bootstrapping learns faster, as it allows us to make updates before we reach the end of an episode. 

#### Cons:
Bootstrapping reduces variance but introduces bias

### Would you expect bootstrapping to help more in blackjack or Easy21?
It really depends how we're representing a game - if we're card counting, then the length of an episode is the time it takes to finish going through a deck of cards, in which case blackjack has significantly longer episodes and could gain a lot more from bootstrapping than Easy21. On the other hand, if our learning agent doesn't want to be kicked out of casinos it's better to represent one round as an episode, and treat the cards in the deck as random. In this case, the lenght of the episode is very short for both blackjack and Easy21, however slightly shorter for blackjack as it doesn't include negative cards. In this case, Easy21 would benefit more from bootstrapping.

Another difference between the two games is that in Easy21 the dealer's behaviour is fixed, whereas in regular blackjack the players have unknown policies. My hypothesis is that since dealer behaviour is fixed, looking ahead with bootstrapping is a lot more stable for Easy21 than blackjack. However potentially bootstrapping could help address the variance in dealer behaviour in blackjack. Honestly, not sure here.

### What are the pros and cons of function approximation in Easy21?

#### Pros:
Function approximation achieved a low MSE after significantly fewer episodes than Sarsa

#### Cons:
Fully representing states rather than features of states allows us to get closer to the true value function. Unless the state space is fully represented by the features, at the optimal solution a slight shift in the value of a feature to more closely fit one state will necessarily worsen the error at another state. 

### How would you modify the function approximator suggested in this section to get better results in Easy21?
With Monte Carlo and Sarsa, the step size (alpha) was dependent on the number of times each step had been visited. With the linear function approximator, we held alpha constant, which may have caused the function approximator to jump around the true value function. Furthermore, a constant small value of alpha will cause very slow progress towards the true value for states that are rarely visited. Thus an improvement could be made by using a varying step size.
