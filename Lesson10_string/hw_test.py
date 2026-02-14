# 3. Reverse a Number and Print Digits
# Task: Write a function reverse_number(number) that takes an integer as input, reverses its
# digits, and prints each digit separated by a space.
# Example:
# Input: number = 1234560
# Output: 0 6 5 4 3 2 1

def reverse_number(number):
	while number > 0:
		last_num = number % 10
		number = number // 10
		print(f'{last_num} ', end='')


reverse_number(1230)

