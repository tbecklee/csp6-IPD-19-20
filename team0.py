####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team0' # Only 10 chars displayed.
strategy_name = 'If greater score'
strategy_description = 'If their score is greater than ours, we betray. '
    
def test(their_score, my_score): 
  if their_score > my_score: 
    return True 
  else: 
    return False

def move(my_history, their_history, my_score, their_score):
   '''Make my move based on the history with this player. history: a string with one letter (c or b) per round that has been played with this opponent. their_history: a string of the same length as history, possibly empty. The first round between these two players is my_history[0] and their_history[0] The most recent round is my_history[-1] and their_history[-1] Returns 'c' or 'b' for collude or betray.''' 
   
   if len(my_history) == 0: 
    return 'c'

   elif test(their_score, my_score) == True: 
     return 'b' 
  
   else: 
     return 'c'


