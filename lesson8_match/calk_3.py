def calculator(number1, number2, action):
	if type(number1) != float and type(number1) != int:
		return "Error: wrong number1 type"
	if type(number2) != float and type(number2) != int:
		return "Error: wrong number2 type"

	match action:
		case "+":
			res = number1 + number2
		case "-":
			res = number1 - number2
		case "*":
			res = number1 * number2
		case "/":
			if number2 == 0:
				res = "Error: number2=0"
			else:
				res = number1 / number2
		case _:
			return "Error: wrong action"
	return res


print(calculator(10, 2, '+'))
print(calculator(10, 2, '-'))
print(calculator(10, 2, '*'))
print(calculator(10, 2, '/'))


print(calculator(10, 0, '/'))
print(calculator('10', 2, '/'))
print(calculator(10, '2', '/'))

print(calculator(10, 2, ''))
print(calculator(10, 2, '1'))
print(calculator(10, 2, '**'))
print(calculator(10, 2, 'a'))


