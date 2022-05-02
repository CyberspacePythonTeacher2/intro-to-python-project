# import random module
import random
# display message
print("Welcome to the game of Rock Paper Scissors.")

#runs without any conditions until the break statement executes inside the loop.
while True:
	print("Enter your choice \n 1 for Rock \n 2 for Paper \n 3 for Scissors \n")
 
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
	print("The user has selected: " + player_select.capitalize())
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

	print(player_select.capitalize() + " Vs " + computer_select.capitalize())
 #for ending the loop
	break