x,y = 10,15

def summary():
	return x + y

print(summary())

def summary1():
	x1 = 5
	y1 = 6
	return x1 + y1

def summary3():
	global x
	global y
	x = 5
	y = 6
	return x + y
summary3()
print(f'second x: {x}')