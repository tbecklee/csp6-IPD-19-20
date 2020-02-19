####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random
import prisoners_dilemma.py

team_name = 'Rush Hour' # Only 10 chars displayed.
strategy_name = 'Betray most of the time and collude randomly'
strategy_description = 'A random generator from '
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    random_value = random.randint(1,number_of_rounds)
    halfway_value = number_of_rounds/2
    if random_value < halfway_value:
      for i in my_history:
        if i % random_value == 0:
          return 'c'
        else:
          return 'b'

  






    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    

