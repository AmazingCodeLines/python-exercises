""" 
Challenge 12-3: Subtraction of Binaries without negatives

	1.	Choose the Random Number Generation Strategy:
	•	Use Python’s random number generation capabilities. You can either generate random integers and convert them to binary or generate 
    random binary digits directly.
	
    2.	Determine Binary Length:
	•	Decide whether you want the binary numbers to be of a fixed length or a variable length. For fixed length, choose a specific number 
    of bits (e.g., 8 bits). For variable length, decide on a range (e.g., 4 to 8 bits) and randomly select a length within that range.
	
    3.	Random Selection for Binary Digits:
	•	To create a binary number, randomly choose 0 or 1 for each bit position. Repeat this process for the total number of bits you have 
    decided on.
	
    4.	Convert Integers to Binary:
	•	If you choose to generate random integers first, convert these integers to binary strings. Remember to format the output so that it 
    doesn’t include any extra prefixes that might be added during conversion.
	
    5.	Ensure Length Consistency:
	•	When converting numbers to binary or generating binary digits directly, make sure that each binary number is formatted to have the 
    desired number of bits, adding leading zeros if necessary.
	
    6.	Testing Binary Generation:
	•	Test the random binary number generator to ensure that it produces binary numbers within the desired length and format consistently.
	
    7.	Integrate with Subtraction Logic:
	•	Before performing subtraction, compare the two binary numbers to ensure the minuend is greater than or equal to the subtrahend.
	•	If the generated numbers do not meet this condition, either swap them or regenerate them to ensure the minuend is always larger.
	
    8.	Handle Borrowing in Subtraction:
	•	Implement logic to handle borrowing, which occurs when subtracting a larger bit from a smaller one in a particular bit position.
	
    9.	Consider Edge Cases:
	•	Consider edge cases such as the subtraction of identical numbers (resulting in zero) and subtraction involving the maximum or minimum 
    binary numbers.
	
    10.	Debug and Refine:
	•	If the binary generation or subtraction logic doesn’t work as expected, debug each part separately to identify and fix any issues.
	
    11.	User Interaction (Optional):
	•	If desired, allow the user to specify the length or range of the binary numbers, enhancing the flexibility of your program.

Additional Tips

	•	Ensure Non-Negative Results:
	•	Implement a check before subtraction to ensure that the first number (minuend) is not smaller than the second number (subtrahend).
	•	If the minuend is smaller, you can either swap the numbers or regenerate them to avoid negative results.
	•	Subtraction Logic:
	•	Handle each bit position starting from the least significant bit (LSB) and proceed to the most significant bit (MSB), managing 
    borrowing where necessary.
	•	Output:
	•	Display the result of the subtraction in binary form, ensuring no leading zeros unless the result is zero.

    The binary subtraction of two bits involves four possible scenarios:

	1.	0 - 0 = 0
	•	Result: 0
	•	Borrow: 0
	
    2.	1 - 0 = 1
	•	Result: 1
	•	Borrow: 0
	
    3.	1 - 1 = 0
	•	Result: 0
	•	Borrow: 0
	
    4.	0 - 1 = 1 (with borrow from the next higher bit)
	•	Result: 1
	•	Borrow: 1 (borrow from the next higher bit)
    """

import random

binary_one_length = random.randint(1, 10)
binary_two_length = random.randint(1, 10)

def check_non_negative_subtraction(binary_one_length, binary_two_length):
    
    while True:
        binary_one = []
        binary_two = []

        decimal_one = 0
        decimal_two = 0

        for i in range(binary_one_length):
            binary_digit = random.choice(["0", "1"])
            binary_one.append(binary_digit)
        
        # to make sure the binary starts with a 1
        binary_one[0] = "1"

        for i in range(binary_two_length):
            binary_digit = random.choice(["0", "1"])
            binary_two.append(binary_digit)

        # to make sure the binary has at least a 1
        binary_two[-1] = "1"

        for i in range(len(binary_one)):
            power = len(binary_one) - 1 - i
            decimal_one += int(binary_one[i]) * (2**power)

        for i in range(len(binary_two)):
            power = len(binary_two) - 1 - i
            decimal_two += int(binary_two[i]) * (2**power)

        if decimal_one > decimal_two:
            return binary_one, binary_two


def check_padding_need(binary_one, binary_two):
    
    max_length = max(len(binary_one), len(binary_two))
    
    padded_binary_one = ["0"] * (max_length - len(binary_one)) + binary_one
    padded_binary_two = ["0"] * (max_length - len(binary_two)) + binary_two

    return padded_binary_one, padded_binary_two


def subtraction_of_binaries(padded_binary_one, padded_binary_two):
    difference_of_binaries = []
    borrow = 0

    for i in range(len(padded_binary_one) - 1, -1, -1):
        
        digit_binary_one = int(padded_binary_one[i])
        digit_binary_two = int(padded_binary_two[i])

        if borrow != 0:
            digit_binary_one -= 1
            borrow = 0

        if digit_binary_one < digit_binary_two:
            digit_binary_one += 2
            borrow = 1
        
        bit_result = digit_binary_one - digit_binary_two
        difference_of_binaries.append(str(bit_result))
    
    difference_of_binaries.reverse()
    
    return ''.join(difference_of_binaries)

# output for control and debug
binary_one, binary_two = check_non_negative_subtraction(binary_one_length, binary_two_length) 
padded_binary_one, padded_binary_two = check_padding_need(binary_one, binary_two)
difference_of_binaries = subtraction_of_binaries(padded_binary_one, padded_binary_two)

print(' '.join(binary_one))
print(' '.join(binary_two))
print("-----------------")
print(' '.join(padded_binary_one))
print(' '.join(padded_binary_two))
print("-----------------")
print(' '.join(difference_of_binaries))