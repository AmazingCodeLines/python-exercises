"""
### Rock, Paper, Scissors Challenge ###

Objective:
Create a Python program that simulates a Rock, Paper, Scissors game where a user plays against the computer. 
The program should prompt the user to input their choice, randomly generate the computer's choice, and then determine and display the winner.


Instructions:

Define the choices using ASCII art.

User Input:

Prompt the user to enter their choice.

Computer Choice:
Randomly select the computer's choice.

Determine the Winner:
Compare user and computer choices to determine the winner.

Display Results:
Show the choices and the winner.

ASCII:

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
"""
import random



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

possible_options = [rock, paper, scissors]
opponent_choice = random.choice(possible_options)
user_choice = int(input("Make your choice.\n[1] Rock\n[2] Paper\n[3] Scissors\n"))


if user_choice == 1:
    print(f"You:\n{rock}")
    if opponent_choice == rock:
        print(f"Opponent:\n {rock}")
        print("It's a draw.")

    elif opponent_choice == paper:
        print(f"Opponent:\n {paper}")
        print("You lost!")
    else:
        print(f"Opponent:\n {scissors}")
        print("You won!")

if user_choice == 2:
    print(f"You:\n{paper}")
    if opponent_choice == rock:
        print(f"Opponent:\n {rock}")
        print("You won!")

    elif opponent_choice == paper:
        print(f"Opponent:\n {paper}")
        print("It's a draw.")
    else:
        print(f"Opponent:\n {scissors}")
        print("You lost!")

if user_choice == 3:
    print(f"You:\n{scissors}")
    if opponent_choice == rock:
        print(f"Opponent:\n {rock}")
        print("You lost!")

    elif opponent_choice == paper:
        print(f"Opponent:\n {paper}")
        print("You won!")
    else:
        print(f"Opponent:\n {scissors}")
        print("It's a draw.")

        