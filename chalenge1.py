
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
