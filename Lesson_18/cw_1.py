# x=10
# y=0
# print(x/y)

# try:
# 	res = x/y
# except ZeroDivisionError:
# 	print('cannot devide by zero')
# print(y/x)

# try:
# 	x = int(input('enter number: '))
# 	print(10/x)
# # except ZeroDivisionError:
# # 	print('cannot devide by zero')
# # except ValueError:
# # 	print('invalid input')
# # except Exception:
# # 	print('error')
# except Exception as e:
# 	print('error', e)

# try:
# 	x = int(input('enter number: '))
# except ValueError:
# 	print('invalid number')
# else:
# 	print('number', x)

try:
	file = open("data1.txt")
	print(file.read())
except FileNotFoundError:
	print('File not found')
finally:
	print('Program ended')

