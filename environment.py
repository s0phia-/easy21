import numpy as np
from config import draw_probs, deck, hit, stick


def draw_number(deck: range = deck):
    number = np.random.choice(deck)
    return(number)


def draw_card(probs_cols: dict = draw_probs):
    # potential card colours and respective probabilities of being drawn
    colors = list(probs_cols.keys())
    probs = [probs_cols.get(x)[0] for x in colors]
    # draw color and number at random
    colour = np.random.choice(colors, p = probs)
    number = draw_number()
    # get and apply colour multiplier
    value = probs_cols.get(colour)[1]
    number = number * value
    return(number)
    

def bust(agent):
    if agent >21 | agent <1:
        return(True)
    else:
        return(False)
        
        
class Easy21:
    
    def __init__(self):
        self.player = draw_number()
        self.dealer = draw_number()
        self.reward = 0
        self.terminal = False

    def dealer_strategy(self):
        if self.dealer < 17 and self.dealer > 0:
            return(hit)
        else:
            return(stick)
        
    def step(self, action):
        assert self.terminal == False
        if action == hit:
            self.player += draw_card()
            if bust(self.player):
                self.terminal = True
                self.reward = -1
        elif action == stick:
            for turns in range(1,1000):
                if self.dealer_strategy() == hit:
                    self.dealer += draw_card()
                else: 
                    self.terminal = True
                    break
            if bust(self.dealer):
                self.reward = 1
            elif self.player == self.dealer:
                self.reward = 0
            elif self.player < self.dealer:
                self.reward = -1
            elif self.player < self.dealer:
                self.reward = 1
        else:
            raise ValueError("Action not recognised")
        if self.terminal:
            self.state = "terminal"
        else:
            state = (self.player, self.dealer)
        return(state, self.reward)