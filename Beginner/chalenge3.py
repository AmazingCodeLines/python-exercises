
"""
Challenge Exercise 3: Python Pizza Deliveries Challenge

Create a Python program that simulates an order for a pizza delivery service. 
The program should calculate the final bill based on the user's choices and display a detailed bill, 
including any extras and delivery costs.
Instructions:

Ask the user for the size of the pizza they want to order (S, M, or L).

Ask the user if they want pepperoni on their pizza (Y or N).

Ask the user if they want extra cheese on their pizza (Y or N).

Generate a random delivery distance between 1 and 20 kilometers.

Calculate the base price of the pizza based on its size:
Small (S): $15
Medium (M): $20
Large (L): $25

Add the cost of pepperoni if the user wants it:
$2 for Small
$3 for Medium and Large

Add the cost of extra cheese if the user wants it:
$1 for any size

Calculate the delivery cost based on the distance:
Free delivery for orders equal to or over $25
Free delivery for distances up to 5 km
$2 for distances up to 10 km
$5 for distances greater than 10 km

Display a detailed bill that includes:
Base price of the pizza
Cost of any extras (pepperoni and extra cheese)
Delivery cost
Total price

Additional Requirements:
Validate the user input to ensure it is correct (S, M, L for size and Y, N for pepperoni and cheese options). 
Prompt the user to enter a valid option if the input is incorrect.


Sample Output:

Thank you for choosing Python Pizza Deliveries!
What size pizza do you want? S, M, or L: M
Do you want pepperoni? Y or N: Y
Do you want extra cheese? Y or N: N
Delivery distance: 8 km


----- Detailed Bill -----
Base price of M pizza: $20
Pepperoni: +$3
Delivery cost: +$2
-------------------------
Total: $25


Hint:
Use loops and functions to validate the user input and to generate the random delivery distance. 
Calculate the total price step by step, and make sure to add the costs of extras and delivery before printing the final bill.

"""

