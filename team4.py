####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'IPD' # Only 10 chars displayed.
strategy_name = 'Remember Betrayal'
strategy_description = 'Colludes first five rounds. After five rounds, only betrays if betrayed more than once in the past five rounds.'

def recent_betrayal_history(their_history):
  '''Determines if program has been betrayed more than once in the past five rounds. Takes the opponent's history as input and outputs either True or False.'''
  recent_betrayal_count = 0
  for i in range(1, 6):
    if 'b' in their_history[-i]:
      recent_betrayal_count += 1
  if recent_betrayal_count >= 2:
    return True
  else:
    return False
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    '''Final Algorithm'''
    if len(my_history) <= 5:
      return 'c'
    else:
      if recent_betrayal_history(their_history) == True:
        return 'b'
      else:
        return 'c'