"""
Challenge Exercise 2: Leap Year Checker

Write a Python program that determines whether a given year is a leap year or not. Your program should meet the following requirements:

Input Handling:
Prompt the user to enter a year.
Ensure the input is a valid integer.
Allow the user to type 'exit' to quit the program.

Leap Year Rules:
A year is a leap year if it is divisible by 4.
However, it is not a leap year if it is divisible by 100, unless it is also divisible by 400.

Output:
If the input year is a leap year, print: "<year> is a leap year."
If the input year is not a leap year, print: "<year> is not a leap year."
If the input is not a valid integer, print: "Please enter a valid integer year.”

Loop:
The program should continuously prompt the user for a year until the user types ‘exit'.


Example Interaction

Enter a year (or type 'exit' to quit): 2000
2000 is a leap year.

Enter a year (or type 'exit' to quit): 1900
1900 is not a leap year.

Enter a year (or type 'exit' to quit): abc
Please enter a valid integer year.

Enter a year (or type 'exit' to quit): 2021
2021 is not a leap year.

Enter a year (or type 'exit' to quit): exit
Exiting the program.


Tips:
Use a while loop to continuously prompt the user.
Use try-except or input validation methods to check if the input is an integer.
Define a function to determine if a year is a leap year for better code organization.

"""