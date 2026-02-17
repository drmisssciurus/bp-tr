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


def is_prime_number(number:int):
	if number > 1:
		count = 2
		sqrt = number ** 0.5
		print(sqrt)
		while count <= sqrt:
			print(count)
			print(number / count)
			if not number % count:
				return False
			count += 1
		return True
	return False


print(is_prime_number(1234567890987654567656732463728374328473))
# print(is_prime_number(2))
# print(is_prime_number(3))
# print(is_prime_number(13))
# print(is_prime_number(125))
