def f3():
	print('start f3', end=' ** ')
	print('end f3', end=' ** ')


def f2():
	print('start f2', end=' ** ')
	f3()
	print('end f2', end=' ** ')


def f1():
	print('start f1', end=' ** ')
	f2()
	print('end f1', end=' ** ')


def main():
	print('start main', end=' ** ')
	f1()
	print('end main', end='')

main()