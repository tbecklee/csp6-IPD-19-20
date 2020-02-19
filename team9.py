team_name = 'Seniors'
strategy_name = 'Sneak Attack'
strategy_description = '''Betray all the turns up until the halfway point, after that collude'''

def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''

    if len(my_history)<150: 
        return 'b'             
    else:
        return 'c'         
    