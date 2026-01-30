def f4():
	print('start f4', end='===>')
	print('end f4', end='===>')


def f3():
	print('start f3', end='===>')
	f4()
	print('end f3', end='===>')


def f2():
	print('start f2', end='===>')
	f3()
	print('end f2', end='===>')


def f1():
	print('start f1', end='====>')
	f2()
	print('end f1', end='')

f1()