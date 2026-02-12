"""
while condition:
	CODE
"""
from lesson5_return.cw5_return1 import result

# x = 0
#
# while x < 5:
# 	print(x)
# 	x += 1
# print('game over')
"""
в тетради
"""

#
# # why while need
# def num_24_to_binary():
# 	number = 24
# 	div_rem = number % 2  # 0
# 	res = str(div_rem)
# 	print(div_rem, end="")
# 	temp = number // 2  # 12
# 	if temp == 0:
# 		return
# 	div_rem = temp % 2  # 0
# 	print(div_rem, end="")
# 	temp //= 2  # 6
# 	if temp == 0:
# 		return
# 	div_rem = temp % 2  # 0
# 	print(div_rem, end="")
# 	temp //= 2  # 3
# 	if temp == 0:
# 		return
# 	div_rem = temp % 2  # 1
# 	print(div_rem, end="")
# 	temp //= 2  # 1
# 	if temp == 0:
# 		return
# 	div_rem = temp % 2  # 1
# 	print(div_rem, end="")
# 	temp //= 2  # 0
# 	if temp == 0:
# 		return
#
#
# num_24_to_binary()
#
#
# def num_24_to_binary():
# 	number = 24
# 	div_rem = number % 2  # 0
# 	res = str(div_rem)
# 	print(div_rem, end="")
# 	temp = number // 2  # 12
# 	if temp == 0:
# 		return res
#
# 	div_rem = temp % 2  # 0
# 	res = str(div_rem) + res
# 	print(div_rem, end="")
# 	temp //= 2  # 6
# 	if temp == 0:
# 		return res
#
# 	div_rem = temp % 2  # 0
# 	res = str(div_rem) + res
# 	print(div_rem, end="")
# 	temp //= 2  # 3
# 	if temp == 0:
# 		return res
#
# 	div_rem = temp % 2  # 1
# 	res = str(div_rem) + res
# 	print(div_rem, end="")
# 	temp //= 2  # 1
# 	if temp == 0:
# 		return res
#
# 	div_rem = temp % 2  # 1
# 	res = str(div_rem) + res
# 	print(div_rem, end="")
# 	temp //= 2  # 0
# 	if temp == 0:
# 		return "\n" + res
#
#
# print(num_24_to_binary())

# with while

def num_to_binary(number:int) -> str:
	if number == 0:
		res = str(0)
	temp = number
	res = ''
	while temp != 0:
		div_rem = temp % 2
		res = str(div_rem) + res
		temp //= 2
	return res

print(num_to_binary(224))
