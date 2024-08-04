"""
Challenge 12-2: Sum Binaries without negatives

Creating a binary calculator that performs arithmetic operations like addition can be an interesting project to develop your understanding 
of binary numbers and how computers perform arithmetic operations. Here are some tips to guide you through the process of coding a binary 
addition calculator:

Understanding Binary Addition

	1.	Binary Addition Rules:
	•	Binary addition works similarly to decimal addition, but it only uses two digits: 0 and 1.
	•	The basic rules for binary addition are:
	•	0 + 0 = 0
	•	0 + 1 = 1
	•	1 + 0 = 1
	•	1 + 1 = 0 (carry 1 to the next higher bit)
	
    2.	Handling Carry:
	•	Like decimal addition, binary addition involves carrying over when the sum of two digits exceeds the base (in this case, 2).
	•	Keep track of the carry and add it to the next higher bit.

Planning the Implementation

	1.	Input Representation:
	•	Decide how you will represent the binary numbers. You can use strings or lists of integers.
	•	Ensure your input validation checks for valid binary input (i.e., consists only of 0s and 1s).
	
    2.	Aligning Inputs:
	•	Binary numbers may have different lengths. Align them by padding the shorter number with leading zeros.
	
    3.	Iterative Addition:
	•	Traverse the binary numbers from right to left (least significant to most significant bit).
	•	Use the binary addition rules to compute the sum for each pair of corresponding bits, considering the carry.
	
    4.	Final Carry:
	•	After processing all bits, check if there is a final carry. If there is, append it to the result.
	
    5.	Result Formatting:
	•	The result may be stored in reverse order (from least to most significant bit). Reverse it to get the correct order.
	•	Convert the result back into a string or desired format for output.

Testing and Edge Cases

	1.	Test Basic Cases:
	•	Test your code with simple binary additions where carry does not occur, such as 01 + 10, and cases where carry is involved, 
    like 11 + 11.
	
    2.	Test Edge Cases:
	•	Consider edge cases like adding zeros (e.g., 0 + 0, 0 + 101).
	•	Test different lengths of binary numbers.
	
    3.	Error Handling:
	•	Handle potential errors, such as non-binary input or empty strings.

Optimizations and Enhancements

	1.	Binary to Decimal Conversion:
	•	For verification, you can convert binary inputs to decimal, perform the addition, and convert the result back to binary to 
    cross-check your results.
	
    2.	Other Operations:
	•	Once addition is working correctly, consider implementing other operations like subtraction, multiplication, and division.
	
    3.	User Interface:
	•	Add a simple user interface for input and output to make your calculator more interactive.
"""

import random


binary_one = []
binary_two = []

binary_one_length = random.randint(1, 10)
binary_two_length = random.randint(1, 10)

for i in range(binary_one_length):
    binary_digit = random.choice(["1", "0"])
    binary_one.append(binary_digit)

for i in range(binary_two_length):
    binary_digit = random.choice(["1", "0"])
    binary_two.append(binary_digit)

def check_padding_need(binary_one, binary_two):
    
    max_length = max(len(binary_one), len(binary_two))
    
    padded_binary_one = ["0"] * (max_length - len(binary_one)) + binary_one
    padded_binary_two = ["0"] * (max_length - len(binary_two)) + binary_two

    return padded_binary_one, padded_binary_two

def sum_of_binaries(padded_binary_one, padded_binary_two):
    added_binaries = []
    carry = 0

    for i in range(len(padded_binary_one) - 1, -1, -1):
        
        digit_binary_one = int(padded_binary_one[i])
        digit_binary_two = int(padded_binary_two[i])

        total = digit_binary_one + digit_binary_two + carry
        result_bit = total % 2
        carry = total // 2

        added_binaries.append(str(result_bit))  

    if carry == 1:
        added_binaries.append(str(carry))

    added_binaries.reverse()

    return ''.join(added_binaries)

padded_binary_one, padded_binary_two = check_padding_need(binary_one, binary_two)

binary_sum = sum_of_binaries(padded_binary_one, padded_binary_two)

print("Binary One:        ", ''.join(binary_one))
print("Binary Two:        ", ''.join(binary_two))
print("Padded Binary One: ", ''.join(padded_binary_one))
print("Padded Binary Two: ", ''.join(padded_binary_two))
print("Sum of Binaries:   ", binary_sum)