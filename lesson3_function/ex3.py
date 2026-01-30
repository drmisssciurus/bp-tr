def main():
	print('start main', end=' ** ')
	f4()
	f1()
	f2()
	print('end main', end='')


def f5():
	print('start f5', end=' ** ')
	print('end f5', end=' ** ')


def f1():
	print('start f1', end=' ** ')
	f3()
	print('end f1', end=' ** ')

	
def f2():
	print('start f2', end=' ** ')
	f6()
	print('end f2', end=' ** ')


def f3():
	print('start f3', end=' ** ')
	f5()
	print('end f3', end=' ** ')


def f4():
	print('start f4', end=' ** ')
	print('end f4', end=' ** ')


def f6():
	print('start f6', end=' ** ')
	f5()
	print('end f6', end=' ** ')

main()

