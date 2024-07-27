"""
Challenge Exercise 2: 

Write a Python program that determines whether a given year is a leap year or not. 
Your program should meet the following requirements:

Input Handling:
Prompt the user to enter a year.
Ensure the input is a valid integer.

Leap Year Rules:
A year is a leap year if it is divisible by 4.
However, it is not a leap year if it is divisible by 100, unless it is also divisible by 400.

Output:
If the input year is a leap year, print: "<year> is a leap year."
If the input year is not a leap year, print: "<year> is not a leap year."
If the input is not a valid integer, print: "Please enter a valid integer year.”

Loop:
The program should continuously prompt the user for a year.

Tips:
Use a while loop to continuously prompt the user.
Use try-except or input validation methods to check if the input is an integer.
Define a function to determine if a year is a leap year for better code organization.

"""

print("Welcome to the leap year checker!")

while True:
    def get_valid_year(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid Input. Please try again.")

    user_year = get_valid_year("Insert a year: ")

    if user_year % 4 == 0:
        if user_year % 100 == 0:
            if user_year % 400 == 0:
                print(f"{user_year} is a leap year.")
            else:
                print(f"{user_year} is not leap year.")
        else:
            print(f"{user_year} is a leap year.")
    else:
        print(f"{user_year} is not leap year.")