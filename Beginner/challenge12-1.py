"""
Challenge 12-1: Create a Decimal to Binary Converter

To convert a decimal number into a binary number, you can follow a systematic approach. Here are some clues to guide 
you through the process:

	1.	Understand Binary Representation:
	•	Binary is a base-2 numeral system, meaning it uses only two digits: 0 and 1.
	•	Each digit in a binary number represents a power of 2, starting from 2^0 at the rightmost position.
	
    2.	Division by 2 Method:
	•	This method involves dividing the decimal number by 2 and keeping track of the remainders.
	•	The binary equivalent is built by the sequence of remainders.
	
    3.	Step-by-Step Process:
	•	Divide the decimal number by 2.
	•	Record the remainder (either 0 or 1). This remainder is the least significant bit (LSB) of the binary number.
	•	Update the decimal number to the quotient from the division.
	•	Repeat the process until the quotient is 0.
	
    4.	Construct the Binary Number:
	•	After the division process is complete, the binary number is constructed by reading the remainders in reverse 
    order (from last to first).
	
    5.	Example:
	•	Think about converting a small number like 10 into binary.
	•	Follow the division process, keeping track of each remainder and updating the number until it reaches zero.
	
    6.	Check Your Work:
	•	Once you’ve determined the binary number, you can verify your result by converting the binary number back to 
    decimal and checking if it matches the original decimal number.
    """
import random

random_decimal = random.randint(1, 100)

def decimal_to_binary(decimal):

    binary = []
    
    while decimal > 0:
            rest = decimal % 2
            binary.append(rest)
            decimal = decimal // 2

    return binary

binary_number = decimal_to_binary(random_decimal)
binary_number.reverse()

print(binary_number)


        




 



