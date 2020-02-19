####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'The Hyenas'
strategy_name = 'Alterate forever if betrayed'
strategy_description = 'Alternate forever if betrayed once, otherwise collude.  If round number is more than 160, betray.'
      
def move(my_history, their_history, my_score, their_score):
  '''Make my move based on the history with this player.
    history: a string with one letter (c or b) per round that has been played with this opponent     their_history: a string of the same length as history, possibly empty      The first round between these two players is my_history[0] and their_history  
    The most recent round is my_history[-1] and their_history  
    Returns 'c' or 'b' for collude or be  .
  '''
  #In this the program colludes until betrayed then betrays forever
  if 'b' in their_history: # If betrayed before
    if len(their_history) % 2 == 0: # Alternates 
      return 'c'
    else:
      return 'b'
  else:
    if len(their_history) > 160: # if they havent betrayed and round past 160, betray
      return 'b'
    else:
      return 'c'