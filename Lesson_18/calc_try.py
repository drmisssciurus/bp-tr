def calculator():
	while True:
		try:
			number1 = float(input("Enter the first number: "))
			break
		except ValueError:
			print("error: wrong number type")

	while True:
		action = input("Enter the operator (+ - * / // %): ").strip()
		if action in ['+', '-', '*', '/', '//', '%']:
			break
		print("error: wrong action try again")

	while True:
		try:
			number2 = float(input("Enter the second number: "))
			break
		except ValueError:
			print("error: wrong number type")

	try:
		if action == "+":
			print("Result: ", number1 + number2)
		elif action == "-":
			print("Result: ", number1 - number2)
		elif action == "*":
			print("Result: ", number1 * number2)
		elif action == "/":
			print("Result: ", number1 / number2)
		elif action == "//":
			print("Result: ", number1 // number2)
		elif action == "%":
			print("Result: ", number1 % number2)
	except ZeroDivisionError:
		print("error: division by zero")


calculator()