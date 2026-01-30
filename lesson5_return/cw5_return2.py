def add():
	a = float(input("Enter first number: "))
	b = float(input("Enter second number: "))
	res = a + b
	return res

result = add()

print(f"result1: {result}")

def add2(a,b):
	return a + b

add2(1, 2)

def coordinates():
	return 10, 20

x,y = coordinates()
print(f"your coordinates is - x: {x}, y: {y}")

