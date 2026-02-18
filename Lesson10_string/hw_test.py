def count_digits(number: int)->int:
	count = 0
	while number != 0:
		count += 1
		number //= 10
	return count

def print_num_column(number:int)->None:
	if type(number) != int or number < 0:
		print('Error')
		return
	temp = number
	count = count_digits(number)
	while count > 0:
		print(temp // (10 ** (count-1)))
		temp = temp % (10 ** (count-1))
		number //=10
		count-=1

print_num_column(1234)