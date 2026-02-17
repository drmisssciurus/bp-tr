# Task 1

def print_digits(number:int)->None:
	if number < 0:
		print("Error: Please enter a positive number.")
	while number > 0:
		print(number%10)
		number//=10

print_digits(1230)
print_digits(-1230)

# Task 2: Check if a number is prime

def is_prime_number(number:int):
	if number > 1:
		count = 2
		sqrt = number ** 0.5
		while count <= sqrt:
			if not number % count:
				return False
			count += 1
		return True
	return False


print(is_prime_number(121))
print(is_prime_number(2))
print(is_prime_number(3))
print(is_prime_number(13))
print(is_prime_number(125))


# Task 3: Lucky Number

def is_lucky_number(number:int)->str:
	count_for_length = 0
	temp = number
	while temp != 0:
		count_for_length += 1
		temp = temp// 10

	calc = 0
	temp_len = count_for_length
	result1 = 0
	result2 = 0
	while calc != count_for_length:
		if temp_len % 2 == 0:
			result1 = number%10 + result1
		else:
			result2 = number%10 + result2
		calc += 1
		temp_len -= 1
		number //= 10
	if result2 == result1:
		return 'luck'
	return 'not luck'


print(is_lucky_number(12345))
print(is_lucky_number(123123))
print(is_lucky_number(123145))
print(is_lucky_number(12121))
print(is_lucky_number(121212))
print(is_lucky_number(2222))
