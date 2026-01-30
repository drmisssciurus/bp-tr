# def outer():
# 	count = 0
# 	print('there is outer')
# 	def inner():
# 		nonlocal count
# 		count+= 1
# 		print(count)
# 	inner()
# 	inner()
# 	inner()
# 	print(count)
#
# outer()

#++++++++++++++++++++++++++++++
# count = 0
# def outer():
# 	global count
# 	count = 1
# 	print('there is outer')
# 	def inner():
# 		nonlocal count
# 		count+= 1
# 		print(count)
# 	inner()
# 	inner()
# 	inner()
# 	print(count)
#
# outer()

def f():
	print('f start')
	def f1():
		print('f1 start')
		def f2():
			print('f2 start')
			print('f2 end')
		f2()
		print('f1 end')
	f1()
	print('f end')

f()

def out():
	a = 5
	print(a)
	def inn():
		a = 2
		print(a)
	inn()
out()