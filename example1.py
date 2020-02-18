####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'xxC3P0xx' # Only 10 chars displayed.
strategy_name = 'C3Po'
strategy_description = 'Collude every third round'



def move(my_history, their_history, my_score, their_score):
  ''' Arguments accepted: my_history their_history are strings. my_score their_score are ints.
  Make my move.
  Returns 'c' or 'b'. 
  '''
  if len(their_history)%11==0:
    return 'c'
  elif my_score>their_score:
    return 'c'
  else:
    return 'b'
