import numpy as np

deck = range(1,11)
# a long explanation on why hit = 0, even though hit obviously has 1 energy:
#
# when we decide on an action, if we are exploiting (rather than exploring),
# we use argmax to pick the action with the highest value. By construction,
# if the values are equal then argmax will return the lowest index. Therefore
# when the values are equal, hit will be chosen by default. This is the preferred
# behaviour, because it encourages the agent to visit states that *require* it
# to hit, i.e. all states where the player hand is above 10. 
# I could have randomized this, but I wanted the agent to go to these states
# (and it's only an issue when the states have equal value)

actions = (hit, stick) = (0, 1)

player_range = range(1,22)
dealer_range = range(1,11)

state_space = (len(player_range), len(dealer_range), len(actions))

draw_probs = {'black': (2/3, 1),
              'red': (1/3, -1)}
terminal = "terminal"

class Easy21:
    
    @staticmethod    
    def draw_number(deck: range = deck):
        number = np.random.choice(deck)
        return(number)  
        
    def __init__(self):
        self.player = Easy21.draw_number()
        self.dealer = Easy21.draw_number()
        self.reward = 0
        self.terminal = False
        self.state = (self.player, self.dealer)
        
    @staticmethod
    def draw_card(probs_cols: dict = draw_probs):
        # potential card colours and respective probabilities of being drawn
        colors = list(probs_cols.keys())
        probs = [probs_cols.get(x)[0] for x in colors]
        # draw color and number at random
        colour = np.random.choice(colors, p = probs)
        number = Easy21.draw_number()
        # get and apply colour multiplier
        value = probs_cols.get(colour)[1]
        number = number * value
        return(number)

    @staticmethod
    def bust(agent):
        if (agent < 1 or agent > 21):
            return True
        else: return False
        
    def dealer_strategy_17(self):
        if self.dealer < 17 and self.dealer > 0:
            return(hit)
        else:
            return(stick)
        
    def step(self, action, terminal = terminal, dealer_strategy = dealer_strategy_17):
        assert self.state != terminal
        if action == hit:
            self.player += Easy21.draw_card()
            self.state = (self.player, self.dealer)
            if Easy21.bust(self.player):
                self.state = terminal
                self.reward = -1
        elif action == stick:
            for turns in range(1,1000):
                if dealer_strategy(self) == hit:
                    self.dealer += Easy21.draw_card()
                    self.state = (self.player, self.dealer)
                else: 
                    self.state = terminal
                    break
            if Easy21.bust(self.dealer):
                self.reward = 1
            elif self.player == self.dealer:
                self.reward = 0
            elif self.player < self.dealer:
                self.reward = -1
            elif self.player > self.dealer:
                self.reward = 1
        else:
            raise ValueError("Action not recognised")
        return(self.state, self.reward)
