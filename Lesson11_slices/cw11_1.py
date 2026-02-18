"""
string[start:stop:step]
start index started (include) 0 stop index end (not include) len
step default 1
"""
text = '11111111'

# print(text[4])
# print(text[:])
# print(text[:5])
# print(text[7:3])
# print(text[7:3:-1])
# print(text[-4])

def reverse_number(number:int)->None:
	if type(number) != int:
		print('Error')
	len_number = len(str(number)) -1
	print(len_number)
	num_to_str = str(number)
	print("'".join(num_to_str[::-1]))

reverse_number(12345)

def print_num_col(num:int)->None:
	if type(num) != int:
		print('Error')
	num_to_str = str(num)
	print("\n".join(num_to_str[::]))
print_num_col(123)