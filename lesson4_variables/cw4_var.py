_var1 = 10
var1 = True
var_var = 6.78
my_name = 'Alina'

print(type(_var1))
print(type(var1))
print(type(var_var))
print(type(my_name))

_var1 = '10'

print(type(_var1))

print('******************')

inp = input('type number')
print(type(inp))
x = int(inp)
print(type(x))


y = float(inp)
print(y)
print(type(y))
print(type(x*1.))

def sum_():
	first = input('enter first number')
	second = input('enter second number')
	summ = int(first) + int(second)
	print(summ)

sum_()
