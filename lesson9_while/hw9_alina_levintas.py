# Exercise 1:

def count_divisible_by_3(number:int)->int:
	count = 0
	if number == 0:
		count += 1
		return count
	while number != 0:
		temp = number % 10
		# if temp == 0:
		# 	number = number // 10
		# 	continue
		if temp % 3 == 0:
			count += 1
		number = number // 10
	return count

print('Exercise 1: ', count_divisible_by_3(120323))
print('Exercise 1.0: ', count_divisible_by_3(0))

# Exercise 2:

def lcm(num1:int, num2:int) -> int:
	if num1 ==0 or  num2==0:
		return "Error: numbers cannot be less than zero"
	count = 1
	while count % num1 != 0 or count % num2 != 0:
		count = count + 1
	return count

print('Exercise 2: ', lcm(12,18))
print('Exercise 2.0: ', lcm(0,0))


# Exercise 3:

def print_stars(count:int) -> None:
	if count <= 0:
		return "Error: count cannot be less than zero"
	res_stars = ''
	star = "*"
	while count > 0:
		res_stars += star
		count -= 1
	print(res_stars)

print("Exercise 3: ", end="")
print_stars(4)
print("Exercise 3.0: ", end="")
print_stars(0)

# Exercise 4
n = 5
res = 1
while n > 1:
	res = res * n
	n -= 1

print("Exercise 4:", res)

# Exercise 5:

def print_stars(stars:int, column:int)->str:
	counter = 0
	result = ''
	if column <= 0 or stars <= 0:
		result = 'Please input number > 0'
		return result
	while counter < stars:
		result += "*"
		counter += 1
		if counter % column == 0:
			result += "\n"
	return result

print("Exercise 5:", print_stars(3, 10))
print("Exercise 5:", print_stars(10, 3))
print("Exercise 5:", print_stars(-3, -10))
