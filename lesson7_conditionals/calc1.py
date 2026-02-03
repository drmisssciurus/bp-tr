def calculator(num1, num2, action):
	if action != "+" and action != "-" and action != "*" and action != "/" and action != "*":
		return "error: wrong action"
	if type(num1) != float and type(num1) != int:
		return "error: wrong type of number 1"
	if type(num2) != float and type(num2) != int:
		return "error: wrong type of number 2"
	if action == "/":
		if num2 == 0:
			return "error: forbitten to divide on 0"
		return num2 / num1
	if action == "*":
		return num1 * num2
	if action == "+":
		return num1 + num2
	if action == "-":
		return num1 - num2
	

print(calculator(20,2,"+"))
print(calculator(20,2,"-"))
print(calculator(20,2,"/"))
print(calculator(20,2,"*"))

print(calculator(20.0,2,"/"))
print(calculator(20,2.0,"/"))
print(calculator('10',20,"/"))
print(calculator(20,'2.0',"/"))




