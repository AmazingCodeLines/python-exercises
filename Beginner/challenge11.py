
# Challenge 11: Hangman part 1

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called word_to_guess.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called choice. Make choice lowercase.

#TODO-3 - Check if the letter the user guessed (choice) is one of the letters in the word_to_guess.



import random

word_list = ["alfa", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliet"]

word_to_guess = random.choice(list(word_list))
print(f"Word to guess (for debuging): {word_to_guess}")

def get_valid_letter(prompt):
    while True:
       user_choice = input(prompt)
       if len(user_choice) == 1 and user_choice.isalpha():
           return user_choice.lower()
       else:
           print("Invalid input. Try again.")

choice = get_valid_letter("Choose a letter: ")

if choice in word_to_guess:
    print("You got it right!")
else:
    print("You got in wrong.")