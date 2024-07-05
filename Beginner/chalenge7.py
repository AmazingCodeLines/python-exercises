
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

user_choice = int(input("Make your choice.\n[1] Rock\n[2] Paper\n[3] Scissors\n"))

opponent_choice = random.choice(possible_options)




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

        