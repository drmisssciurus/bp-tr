# 1. Fan Mode Control Function

def fan(mode):
	# if type(age) != int: такой вариант, но я хотела потренировать с not
	if not (type(mode) == int):
		print("Error1: Invalid mode. Please enter number 0, 1, 2, or 3.")
		return
	if (0 > mode) or (mode > 3):
		print("Error2: Invalid mode. Please enter 0, 1, 2, or 3.")
		return
	if mode == 0:
		print("Fan is turned off.")
	if mode == 1:
		print("Fan is running at speed 1")
	if mode == 2:
		print("Fan is running at speed 2")
	if mode == 3:
		print("Fan is running at speed 3")

fan("1")
fan({1})
fan(0)
fan(1)
fan(2)
fan(3)
fan(4)
fan(-1)

print("*************************************")

# 2. Even or Odd Checker

def even_or_odd(number):
	if not (type(number) is int):
		print("Error: Invalid mode. Please enter 0, 1, 2, or 3.")
		return
	if number % 2:
		print("The number is odd.")
		return
	print("The number is even.")


print('1')
even_or_odd(1)
print('2')
even_or_odd(-2)
print('3')
even_or_odd(-3)
print('4')
even_or_odd(4)
print('5')
even_or_odd('5')
print('6')
even_or_odd(6)
print('7')
even_or_odd(0)

print("*************************************")

# 3. Age Group Classification

def my_age(age):
	if not (type(age) == int):
		print("Error: Invalid mode. Please enter a number.")
		return
	if age < 0:
		print("Error: Age cannot be negative.")
		return
	if age <= 18:
		print("Child.")
		return
	if age <= 67:
		print("Adult.")
		return
	if age <= 120:
		print("Retired.")
		return
	print("Ancient.")


print('1')
my_age('18')
print('2')
my_age(-18)
print('3')
my_age(0)
print('4')
my_age(10)
print('5')
my_age(19)
print('6')
my_age(50)
print('7')
my_age(99)
print('8')
my_age(140)
