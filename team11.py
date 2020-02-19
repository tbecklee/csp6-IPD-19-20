####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

import random
team_name = 'Chernobyl Team' # Only 10 chars displayed.
strategy_name = 'Probability'
strategy_description = 'Betray 75% of the time and collude 25% of the time'

def move(my_history, their_history, my_score, their_score):
    ''' This strategy plays betrayal 75% of the time and plays collude 25% of the time.
    '''
    
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].  
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    if random.randint(0, 100) >= 75:
      return 'b'
    else:
      return 'c'
