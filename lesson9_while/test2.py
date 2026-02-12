# Exercise 5:
# Task:
# Create a function print_stars(stars, column) that prints a specified number of stars in
# multiple rows. The number of columns is determined by the column parameter.
# Remaining stars that don't fill a row will appear in the last row.
# Example:
# print_stars(10, 4)

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

print(print_stars(3, 10))
print(print_stars(10, 3))
print(print_stars(-3, -10))


