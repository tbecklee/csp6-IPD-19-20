
'''Information and description on this strategy.'''
team_name = 'Kaitlyn and Ishan'
strategy_name = 'Random (leaning collude)'
strategy_description = 'Random choice. 66% chance of colluding, 33% chance of betraying.'

import random

def move(my_history, their_history, my_score, their_score):
  '''Makes choice based on weighted random choice (but leans towards colluding) Does not account for opponent's or self's history since it always chooses randomly. 
  
  their_history: a string of the same length as history, possibly empty. 
  The first round between these two players is my_history[0] and their_history[0]
  The most recent round is my_history[-1] and their_history[-1]
    
  Returns 'c' or 'b' for collude or betray.
  '''
  random_choice = random.randint(0,4)
  if random_choice >= 2:
    return 'c'
  else:
    return 'b'
    
'''Since the strategy uses a weighted random choice, it doesn't need to know any information about itself or it's opponent's past history.'''

move(0,0,0,0)#Calls the function with appropriate starting values