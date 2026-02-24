# Task 3: Lucky Number
def count(number):
	count=0
	while number != 0:
		count += 1
		number = number// 10
	return count

def is_lucky_number_sides(number:int)->str:
	i = count(number)
	if i % 2 != 0:
		error = 'error: number should have equal number of numbers for both sides'
		return error
	sum_ = 0
	while i > 0:
		sum_ += (number//10**(i-1)) - number%10
		number -= (number//10**(i-1))*10**(i-1)
		number //= 10
		i-=2
	return 'luck' if sum_ == 0 else 'not luck'

#
# print(123%10)
# print(123//100)

print(is_lucky_number_sides(12300321))
print(is_lucky_number_sides(123442321))
print(is_lucky_number_sides(122334423521))


# Task 3: Lucky Number
def count(number):
	count=0
	while number != 0:
		count += 1
		number = number// 10
	return count

def is_lucky_number_sides(number:int)->str:
	i = count(number)
	if i % 2 != 0:
		error = 'error: number should have equal number of numbers for both sides'
		return error
	sum_ = 0
	while i > 0:
		sum_ += number%10
		number //= 10
		sum_ -= number%10
		number//=10
		i-=2
	return 'luck' if sum_ == 0 else 'not luck'

#
# print(123%10)
# print(123//100)

print(is_lucky_number_sides(12300321))
print(is_lucky_number_sides(123442321))
print(is_lucky_number_sides(122334423521))
