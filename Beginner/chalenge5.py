'''
Chalenge Exercise 5: 

Create a Text-Based Adventure Game

In this exercise, you will create a text-based adventure game called "Treasure Island." 
The goal of the game is to guide the player through a series of choices to find a hidden treasure. 
Follow the steps below to build the game:

Step 1: Print the Game Introduction
Start by printing a welcome message and the mission statement for the game.
Include a separator line to visually separate the introduction from the game instructions.

Step 2: Get the First User Choice
Prompt the player with a situation where they need to get to an island in the middle of a lake.
Provide three options: waiting for a boat, swimming across, or giving up.
Ensure the player's input is converted to lowercase for consistency.

Step 3: Handle the First User Choice
Use conditional statements to handle each possible input from the player.
If the player chooses to give up, print a message indicating the game is over and exit the game loop.
If the player chooses to swim across, print a message indicating the player failed and end the game.
If the player chooses to wait for a boat, print a message indicating the player successfully used a boat to cross the lake 
and proceed to the next choice.

Step 4: Get the Second User Choice
If the player successfully crosses the lake, prompt them with a new situation involving a house with colored doors.
Provide three options: opening a yellow door, opening a red door, or giving up.
Ensure the player's input is converted to lowercase for consistency.

Step 5: Handle the Second User Choice
Use a loop to repeatedly prompt the player until they provide a valid input.
If the player chooses to give up, print a message indicating the game is over and exit the game loop.
If the player chooses the yellow door, print a message indicating the player failed and end the game.
If the player chooses the red door, print a message indicating the player found the treasure and end the game.
If the player provides an invalid input, print an error message and prompt them to try again.

Additional Tips:
Test your game thoroughly to ensure all input paths work correctly.
Consider adding more choices and branches to make the game more complex and interesting.
Use functions to organize your code better if the game becomes larger.

Final Task:
Implement the game based on the instructions above.
Make sure to handle all possible inputs and guide the player through the choices smoothly.
Good luck, and have fun coding!

'''



print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("________________ > > ________________")

    
while True:
    choice_1 = input("You need to get to the island, that is in the middle of a lake.\n"
                    "If you want to wait for a boat, type 'boat.\n"
                    "If you want to swim across, type: 'swim'.\n"
                    "If you want to give up, type 'exit'.\n").lower()

    if choice_1 == 'exit':
        print("You chose to give up. The game is over.")
        break

    elif choice_1 == "swim":
        print("Next time better learn to swim first. The Game is Over!")
        break

    elif choice_1 == "boat":
        print("Against all odds, you see a boat and use it to cross.")
        print("________________ > > ________________")
        
        while True:
            choice_2 = input("You see a house with coloured doors. Now you face another choice.\n"
                    "To open the yellow door, type 'yellow'\n"
                    "To open the red door, type 'red'\n"
                    "to give up, type 'exit'.\n").lower()
            
            if choice_2 == 'exit':
                print("You chose to give up. The game is over.")
                break
            
            elif choice_2 == "yellow":
                print("Next time better choose the other door. The Game is Over!")
                break

            elif choice_2 == "red":
                print("You used your 50/50 card wisely. You found the treasure.\n"
                      "Game over. Spend it well.")
                break

            else:
                print("That is not a valid input. Please try again.")
                print("________________ > > ________________")

        break
    
    else:
        print("That is not a valid input. Please try again.")
        print("________________ > > ________________")
        
        





