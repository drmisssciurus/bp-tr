# number = input('enter number: ')
# operator = input('enter operator + - / *: ')
# number2 = input('enter number: ')
# def calculator(a, b, c):
# 	result = a + b + c
# 	return eval(result) #нельзя употреблять отдаст все коды от всего
#
# print(calculator(number, operator, number2))


radius = float(input('enter radius: '))
side = float(input('enter side: '))
side1 = float(input('enter side1: '))
side2 = float(input('enter side2: '))
def common_sq(a, b, c, d):
	result = f'Common Square is {(circle_sq(a) + sq_sq(b) + req_sq(c,d)):.2f}'
	return result

def circle_sq(a):
	res = 3.14 * a**2
	return res

def sq_sq(b):
	res = b**2
	return res

def req_sq(c, d):
	res = c*d
	return res

print(common_sq(radius, side, side1, side2))