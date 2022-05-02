# variable declaration
player_choice = "paper"
is_player_win = True
current_round = 0
number_of_rounds = 3

def computer_play():
  return "rock" # Good ol rock, nothing beats that

# display message
print("Welcome to the game of Rock Paper Scissors.")

while current_round != number_of_rounds: # while loop with condition
  print("Current round: " + str(current_round + 1)) # we should show 1 instead of 0 for the first round
  computer_choice = computer_play()

  # display choices
  print("Player's choice: " + player_choice)
  print("Computer's choice: " + computer_choice)

  current_round = current_round + 1 # operator to manipulate the round number

# display whether player wins
print("Player win status: " + str(is_player_win)) #this will print True, we have to typecast to string