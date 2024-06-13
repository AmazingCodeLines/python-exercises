"""
Challenge Exercise 1: Tip Calculator with Input Validation

Objective:

Create a tip calculator program that prompts the user for the total bill amount, the desired tip percentage, 
and the number of people to split the bill. 
The program should validate user inputs to ensure they are numbers that can be used in the calculations. 
Finally, the program should output the calculated tip, total bill, and the amount each person should pay.

Requirements:
Welcome Message: Display a welcome message to the user.

Input Prompts:
Ask the user for the total bill amount.
Ask the user for the tip percentage they would like to give.
Ask the user for the number of people to split the bill.

Input Validation:
Ensure that the total bill amount and tip percentage are valid floating-point numbers.
Ensure that the number of people to split the bill is a valid integer.
If an invalid input is entered, prompt the user again until a valid input is received.

Calculations:
Calculate the tip amount based on the bill and tip percentage.
Calculate the total bill including the tip.
Calculate the amount each person should pay.

Output:
Display the original bill amount.
Display the calculated tip amount.
Display the total bill amount (bill + tip).
Display the amount each person should pay.
"""




print("Welcome to the Tip calculator!")

# Function to check the user's input for a float, if it is False, asks for a valid input
def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid Input. Please try again.")

# Function to check the user's input for an integer, if it is False, asks for a valid input
def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid Input. Please try again.")

bill = get_valid_float("What was the total bill?\n$")
tip = get_valid_float("What percentage tip would you like to pay?\n%")
people = get_valid_int("How many people are splitting the bill?\n")

tip_amount = bill * (tip / 100)
total_bill = bill + tip_amount
bill_per_person = total_bill / people

print(f"Your bill is ${round(bill, 2)}")
print(f"The tip is ${round(tip_amount, 2)}")
print(f"The total bill is ${round(total_bill, 2)}")
print(f"Each person should pay: ${round(bill_per_person, 2)}")