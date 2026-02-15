# Task 2: Check if a number is prime
# Write a function is_prime_number(number) that takes an integer as input. If the number is
# prime, the function should return True; otherwise, return False.
# Definition of a prime number:
# A prime number is greater than 1 and has no divisors other than 1 and itself.
# Example Input and Output:
# Input: 7
# Output: True (7 is prime)
# Input: 8
# Output: False (8 is divisible by 2 and 4)
# Input: 1
# Output: False (1 is not prime)
from itertools import count


def is_prime_number(number:int):
	if number <= 0:
		return False
	count = 1
	while count * count < number:

	return True
print(2%2)
print(is_prime_number(1))
print(is_prime_number(2))
print(is_prime_number(4))
print(is_prime_number(13))
