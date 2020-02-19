####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = '	USSAadi' # Only 10 chars displayed.
strategy_name = 'Betray_Till-Confirm_Colluder'
strategy_description = 'We betray until the opponent colludes twice in a row or has a collude rate of 70% or higher'
    
def check_betrayal(history):
	'''based on this players history, returns True if it he is a betrayer and False if he is a colluder'''
	b_counter, c_counter = 0, 0
	for letter in history:
		if(letter == 'b'):
			b_counter += 1
		else:
			c_counter += 1
	if(b_counter/len(history) >= .7):
		return True
	else:
		return False


def move(my_history, their_history, my_score, their_score):
	'''Make my move based on the history with this player.

	history: a string with one letter (c or b) per round that has been played with this opponent.
	their_history: a string of the same length as history, possibly empty. 
	The first round between these two players is my_history[0] and their_history[0]
	The most recent round is my_history[-1] and their_history[-1]

	Returns 'c' or 'b' for collude or betray.
	'''
	#reference strategy description 
	if(len(their_history) >= 2):     
		if(check_betrayal(their_history)):
			return 'b'
		else:
			return 'c'
	else:
		return 'b'#because betraying is good

