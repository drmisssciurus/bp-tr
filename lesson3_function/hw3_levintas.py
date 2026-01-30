"""
1. Answer the three questions on slide 13. Note that we only count the functions we write,
   not the library functions.

	1. How many functions are called by "main"? - 3 functions are called by "main"
	2. Which functions are not called? - only Function 3 are not called
	3. Which functions do not call any other functions? - Function 3 and Function 6 do not call any other functions
"""

# ************************************************************************************

"""
2. write code that will output the following to the console (slide 13)
"""

def main():
	print('main()', end=' ')
	function6()
	print('main()', end=' ')
	function1()
	print('main()', end=' ')
	function2()


def function5():
	print('f5()', end=' ')
	function6()


def function1():
	print('f1()', end=' ')
	function4()


def function2():
	print('f2()', end=' ')
	function6()


def function3():
	return


def function4():
	print('f4()', end=' ')
	function5()


def function6():
	print('f6()', end='\n')


main()

# ************************************************************************************

"""
3. dialog
   write a function that will use the input and on the console it will look like this...
	Your name: Alina
	Your name: Alina
	info: programmer
	info: programmer
	Your group: BP-35
	Your group: BP-35
"""

def dialog():
	print("Your name:", input("Your name:"))
	print("info:", input("info:"))
	print("Your group:", input("Your group:"))

dialog()

