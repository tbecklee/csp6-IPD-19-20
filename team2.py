####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = '10 chars' # Only 10 chars displayed.
strategy_name = 'Arithmetic Progression'
strategy_description = 'Check if the opponent uses arithmetic progression or retaliates, or both'
    
def move(my_history, their_history, my_score, their_score):

  ''' 
  Arguments accepted: my_history, their_history are strings.
  my_score, their_score are ints.
  
  Make my move.
  Returns 'c' or 'b'. 
  '''

  '''
  Strategy 1:
  If a person's last move is betray, they are less likely to betray the next round
  As they keep betraying, they are less and less likely to betry
  If the betray past a certain threshold, it becomes more and more clear that they're just doing one move. In that case, bring them down with you

  Always betray the first time, as programs are most likely to collude
  Track how likely they are to betray as the game goes on, usually goes up
  Track how likely they are to betray the next round, usually goes down

  Strategy 2:
  Always collude for the first 10 moves, regardless of what the opponent does
  Split the dataset 7:3
  Train the dataset, and then store the loss in the testing phase in a file
  Feature 1: Current round (can help detect iterative algorithms)
  Feature 2: State (collude or betray)
  https://www.datacamp.com/community/tutorials/k-nearest-neighbor-classification-scikit-learn

  Strategy 3:
  It is likely that some, if not most, groups will use simple arithmetic progression and retaliate after the previous group has betrayed.
  A take on the retaliation theory and how to combat it is on line 98.
  Therefore, we need to check whether they use arithmetic progression or retaliation, or both
  '''

  # my_history: a string with one letter (c or b) per round that has been played with this opponent.
  # their_history: a string of the same length as history, possibly empty. 
  # The first round between these two players is my_history[0] and their_history[0].
  # The most recent round is my_history[-1] and their_history[-1].
  
  # Analyze my_history and their_history and/or my_score and their_score.
  # Decide whether to return 'c' or 'b'.

  # honestly I feel that this strategy is going to be absolutely terrible

  '''
  This is particularly inefficient since it calculates this every time the function runs
  A more efficent method would be to save this data to a JSON file and parse the file everytime
  This method is alright since we don't really care about optimizations for now
  '''
  foundb = False
  retaliates = False

  retaliatedOnEven = False; # this can be used to determine the next move
  iterator = 0
  count = 0
  
  if len(their_history) < 10:
    return 'b'

  # ideally, this should only be done at the start of the round after 10 matches and saved to a file but it's alright
  while (iterator < 10):
    if their_history[iterator] == 'b' and foundb == False:
      if (iterator % 2) == 0:
        retaliatedOnEven = True
      else:
        retaliatedOnEven = False
      
      foundb = True
      count += 1
    else:
      break;

    iterator += 1

  # epic test to see if they react
  if not (len(my_history) > 0 and len(my_history) < 1):
    # use the third item since people usually betray on the first try
    # We need figure out if they retaliate to our
    if (my_history[2] == 'b' and their_history[2] == 'b') and not ((len(my_history) + 1) % count) == 0:
      retaliates = True
    else:
      retaliates = False


  '''
  Running a modulus on len(my_history) + 1 will check the current round. This can be used to check if we should act on the round we are supposed to
  Running a modulus on len(my_history) - 1 will check if the current round is something we should act on by checking the previous round

  Normal Retaliation Scheme (They retaliate first)
  ------------------------------------------------
  Them: cccbcbcbcbcbcbc
  You:  ccccbcbcbcbcbcb
  
  Right now, one person is at a disadvantage because old information about the retaliation is being used.
  They will both betray when the other colludes, assuming infinite retaliation
  The problem with this is that the reward matrix will favor one person or the other, but neither has the team number of the other team
  Because of this, it is impossible to decide if the reward matrix will favor you or not. (I mean you can probably use the score to figure it out, but that would require a sample size)

  Better Retaliation Scheme (They retaliate first)
  ------------------------------------------------
  Them: cccbcbcbcbcbcbc
  You:  cccccbcbcbcbcbc

  With this scheme, you collude twice more, but then you match their movements, even with outdated information.
  No matter who the reward matrix favors, you will certainly bring the other person down with you by mirroring their movements

  NOTE: this strategy will only work if a retaliation loop is entered. For example, if the other team does:
  ```
  if their_history[-1] == 'b':
    return 'b'
  else:
    return 'c'
  ```

  If they somehow exit the retaliation loop, it will continue to betray every other round regarless of if they stopped
  This could be combatted by having persistent storage but that's alright.
  It is very likely that once they enter a retaliation loop, they will not exit, so this strategy should hold firm. I do not think anyone would do that.
  '''

  # hopefully this works
  if retaliates:
    if retaliatedOnEven: # if the last round is odd and they first retaliated on an even number, this round is even so retaliate
      if len(my_history) - 1 % 2 == 1:
        return 'b'
      else:
        return 'c'
    else:
      if len(my_history) - 1 % 2 == 0: # if the last round is even and they first retaliated on an even, this round is odd so retaliate
        return 'b'
      else:
        return 'c'
    #return 'b' # bring them down with you
  else: # they do not retaliate to our moves, at least we think they do not
    if ((len(my_history) + 1) % count) == 0: # if our next move is going to be where they betray, betray aswell
      return 'b'
    else: # if our next move is not going to be where they betray, then follow the normal 5 round betray convention
      if ((len(my_history) + 1) % 5) == 1:
        return 'b' 
      else:
        return 'c'
    
  return 'c' # if all else fails