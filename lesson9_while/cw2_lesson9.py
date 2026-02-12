def num_to_binary(number:int) -> str:
	if number == 0:
		res = str(0)
		return res
	temp = number
	res = ''
	count = 0

	while temp != 0:
		div_rem = temp % 2
		if count != 0 and count % 4 == 0:
			res = " " + res
		# if  count % 4 != 0:
		# 	res = '0' + res
		res = str(div_rem) + res
		temp //= 2
		count += 1
		print(count)
	return res

# print(num_to_binary(224))
# print(num_to_binary(0))
print(num_to_binary(1300))
