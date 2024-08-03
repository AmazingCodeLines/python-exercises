"""
Challenge 12: Create a Binary to Decimal Converter

Objective:

Write a Python function that converts a binary string into its decimal equivalent. The function should be able to take any valid binary number 
(a string of 0s and 1s) and return the corresponding decimal number, formatted with underscores as thousands separators.

Instructions:

	1.	Function Definition:
	•	Define a function named binary_to_decimal that accepts a single parameter binary, which is a string representing a binary number.
	
    2.	Initialize Decimal Value:
	•	Inside the function, initialize a variable decimal to zero. This will store the resulting decimal number.
	
    3.	Iterate Over Binary String:
	•	Use a loop to iterate over each character (digit) in the binary string from left to right.
	•	For each digit, calculate its contribution to the decimal number:
	•	Convert the character to an integer (either 0 or 1).
	•	Calculate the power of 2 that corresponds to the digit’s position in the string (from right to left).
	
    4.	Update Decimal Value:
	•	Multiply the integer digit by 2 raised to the power of its position.
	•	Add the result to decimal.
	
    5.	Return the Decimal Result:
	•	After processing all digits, return the final decimal value.
	
    6.	Test the Function:
	•	Create a binary number as a string, for example, "1010".
	•	Call your function with this binary string and store the result in a variable.
	•	Print the decimal result using an f-string, formatted with underscores as thousands separators.

"""

binary_number = "1010"

def binary_to_decimal(binary):

    decimal = 0
    
    for i in range(len(binary)):

        power = len(binary) - i - 1
        decimal += int(binary[i]) * (2 ** power)
    
    return decimal


decimal_number = binary_to_decimal(binary_number)
print(f"The decimal equivalent of binary {binary_number} is {decimal_number:_}")