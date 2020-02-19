####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Omega' # Only 10 chars displayed.
strategy_name = 'Tit for Tat with override'
strategy_description = 'Will return the opponenet\'s last move, with a 5% chance of b, and a 5% chance of c'

import random

def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    
    #This example player plays their opponent's last move with a 5% chance of returning c and a 5% chance of returning b.
    if len(my_history) == 0:
      return random.choice(["c", "b"])
    else:
      if random.randint(1,20) == 20:
        return "c"
      elif random.randint(1, 20) == 20:
        return "b"
      else:
        return their_history[-1]