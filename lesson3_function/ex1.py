def main():
	print('start main', end='===>')
	f3()
	f1()
	f2()
	f3()
	print('end main')


def f3():
	print('start f3', end='===>')
	print('end f3', end='===>')


def f2():
	print('start f2', end='===>')
	print('end f2', end='===>')


def f1():
	print('start f1', end='====>')
	print('end f1', end='')

main()
main()
