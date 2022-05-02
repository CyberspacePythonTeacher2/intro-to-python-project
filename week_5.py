# import random module
import random

#variable initialization
points_to_win = 0
player_score = 0
computer_score = 0
player_select = ''
computer_select = ''

# function if player wins round
def player_win_round():
  global player_score
  player_score += 1
  print(player_select.capitalize() + " Vs " + computer_select.capitalize() + ", Player wins the round!")

# function if computer wins round
def computer_win_round():
  global computer_score
  computer_score += 1
  print(player_select.capitalize() + " Vs " + computer_select.capitalize() + ", Computer wins the round!")

# function for the computer selection
def get_computer_selection():
  global computer_select

  print("\nComputer's turn.......")

  #We make a specific interval that the computer choose a random  number between (1,3)
  computer_choice = random.randint(1, 3)

  # It is okay if the computer makes the same choice

  if computer_choice == 1:
    computer_select = 'rock'
  elif computer_choice == 2:
    computer_select = 'paper'
  else:
     computer_select= 'scissors'

  print("Computer has selected: " + computer_select.capitalize())

def get_player_selection():
  global player_select
  print("\nEnter your choice: \n 1 for Rock \n 2 for Paper \n 3 for Scissors \n")
 
 	# take the input from the user for making a selection
  player_choice = int(input("Player's turn: "))
 
 #looping until user enter invalid input
  while player_choice > 3 or player_choice < 1:
     player_choice = int(input("Your input is not valid, please enter a value between 1,3: "))
		
  if player_choice == 1:
    player_select = 'rock'
  elif player_choice == 2:
    player_select = 'paper'
  else:
    player_select = 'scissors'

  # print user choice
  print("The player has selected: " + player_select.capitalize())


# display message
print("Welcome to the game of Rock Paper Scissors.")

print("Enter the amount of points to win.")
# take the input from the user for the amount of points to win
points_to_win = int(input("Points to win: "))

#runs the loop as long as the player points or computer 
while player_score < points_to_win and computer_score < points_to_win:
	
  get_player_selection()
  get_computer_selection()

  if player_select == computer_select:
    print(player_select.capitalize() + " Vs " + computer_select.capitalize() + ", It's a draw!")
  elif player_select == 'paper' and computer_select == 'rock':
    player_win_round()
  elif player_select == 'rock' and computer_select == 'scissors':
    player_win_round()
  elif player_select == 'scissors' and computer_select == 'paper':
    player_win_round()
  else:
    computer_win_round()

  print("\nThe score is " + str(player_score) + " to " + str(computer_score))

if player_score == points_to_win:
  print("\nPlayer wins the game!")
else:
  print("\nComputer wins the game!")
