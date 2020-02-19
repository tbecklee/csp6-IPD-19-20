####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Pranav and Natalie' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    

def move( my_score, their_score):
    '''makes move based on the comparison of my score to their score
    '''
    if my_score <= their_score:
      return 'b'
    else:
      return 'c'
