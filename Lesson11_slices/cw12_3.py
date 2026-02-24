x = '12345678 '
x2 = 12345678
def sum_even_digits(number:str)->int:
	if type(number) != str or not number.strip().isdigit():
		print('wrong type')
		return -1
	summ_=0
	for i in number.strip():
		if int(i) % 2 == 0:
			summ_+=int(i)
	return summ_

# print(sum_even_digits(x))

def sum_pos_even_digits(number:str)->int:
	if type(number) != str or not number.strip().isdigit():
		print('wrong type')
		return -1
	summ_=0
	strip_num = number.strip()
	step = 2

	for i in range(0, len(strip_num), step):
			summ_+=int(strip_num[i])
	return summ_

# print(sum_pos_even_digits(x))

step = 5
for i in range(step):
	print(i)