# Rock Paper Scissors
Repo for the project based approach of Intro to Python Bootcamp.

- [Rock Paper Scissors](#rock-paper-scissors)
  - [Introduction](#introduction)
  - [Before Starting](#before-starting)
  - [Week 1](#week-1)
  - [Week 2](#week-2)
  - [Week 3](#week-3)
  - [Week 4](#week-4)

## Introduction

In this project we are going to do a simple implementation of the game "Rock Paper Scissors" (aka **Schere, Stein, Papier** in German).
It is a game that can be played between two or more players. The players can choose either “rock, paper, scissors”. Then each of the players simultaneously makes their hands in the shapes of Rock Paper Scissors.
Some of you who might not know the game can check the [Wikipedia](https://en.wikipedia.org/wiki/Rock_paper_scissors) or this hilarious [Wikihow](https://www.wikihow.com/Play-Rock,-Paper,-Scissors). The game will be played in the command line interface.
The winner is selected based on the following:

-Rock smashes scissors.
-Paper covers rock.
-Scissors cut paper.


## Before Starting

1. Set up the project location using PyCharm where you will be doing the project. 
2. Test by using `print("Hello, World!")` (you know, for good luck 😊).
3. Commit and push your changes to the repository of your project.

## Week 1

Since in the first week we only learn to set up the development environment and did the Hello World exercise, we are going to implement the introduction message when we start the project program. It can be something as simple as 
```
Welcome to the game of Rock Paper Scissors.
```
or it can be as epic as
```
The year is 20xx. The world is overrun by rogue AIs. You are now face to face with the hive mind of all the AIs, the RPS. The world hangs in balance on the game of Rock Paper Scissors that you are going to play against RPS.
```
It is up to you how you want to introduce to the player that runs your project.

Code snippet for this week:
```python
print("Welcome to the game of Rock Paper Scissors.")
```

## Week 2

Now that we've learnt about Variables and Booleans in week two, we are going to introduce these two elements into our project. We will add variables for the player's choice and also the computer's choice.

Code snippet:
```python
computer_choice = "rock" # Good ol rock, nothing beats that
player_choice = "paper"

print("Player's choice: " + player_choice)
print("Computer's choice: " + computer_choice)
```

Since we have learned about Booleans in week two, we can also use booleans as a way to keep track of whether the player won or not.

Code snippet:
```python
is_player_win = True
print("Player win status: " + str(is_player_win))  #this will print True, we have to typecast to string
```

We can then structure the whole code to be more organized. The code snippet up to this point should look something like below.

Code snippet for this week:
```python
# variable declaration
computer_choice = "rock" # Good ol rock, nothing beats that
player_choice = "paper"
is_player_win = True

# display message
print("Welcome to the game of Rock Paper Scissors.")

# display choices
print("Player's choice: " + player_choice)
print("Computer's choice: " + computer_choice)

# display whether player wins
print(is_player_win)
```

## Week 3

In this week we learnt about loops, operators and conditions and we will introduce them to our project up to this point. We also learnt about functions, then we can introduce them to the project as well.

For the loops, we are going to use it to control how many rounds are played. We will also use operators to manipulate the round number and we use condition to determine when the while loop is exited.

Code snippet:
```python
current_round = 0
number_of_rounds = 3

while current_round != number_of_rounds: # while loop with condition
  print("Current round: " + str(current_round + 1))
  current_round = current_round + 1 # operator to manipulate the round number
```

As for function, we are going to make a function where the computer will make it's choice to play against the player.

Code snippet:
```python
def computer_play():
  return "rock" # Good ol rock, nothing beats that
```

We can then combine the code snippets below with the rest of our code.

Code snippet for this week:
```python
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
```

## Week 4

``` python

```

