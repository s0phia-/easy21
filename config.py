# configuration file for easy 21 game, following rules here:
# https://www.davidsilver.uk/wp-content/uploads/2020/03/Easy21-Johannes.pdf

deck = range(1,11)
actions = (hit, stick) = (0, 1)

dealer_range = range(1,11)
player_range = range(1,21)

state_space = (len(dealer_range), len(player_range), len(actions))

draw_probs = {'black': (2/3, 1),
              'red': (1/3, -1)}

