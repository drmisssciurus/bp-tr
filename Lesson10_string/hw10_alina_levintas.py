# 1. Character Count Function

def char_count(string:str, char:str)->int:
		len_char = len(char)
		if len_char != 1:
			return -1
		new_string = string.lower()
		new_char = char.lower()
		count = len(string) - 1
		result = 0
		while count >= 0:
			if new_string[count] == new_char:
				result += 1
			count -= 1
		return result


print('Ex1: ', char_count('Alina','a'))
print('Ex1: ', char_count('Alina','b'))
print('Ex1: ', char_count('1111','1'))
print('Ex1: ', char_count('1111','12'))

# 2. Print String with Spaces

def print_str_with_space(str:str)->str:
	str_len = len(str) - 1
	result = ''
	count = 0
	while count <= str_len:
		result += str[count] + " "
		count += 1
	return result

print('Ex2: ', print_str_with_space("hello"))


# 3. Reverse a Number and Print Digits

def reverse_number(number):
	num_to_str = str(number)
	num_len = len(num_to_str) - 1
	result = ''
	while num_len >= 0:
		result += num_to_str[num_len] + ' '
		num_len -= 1
	return result

print('Ex3: ',reverse_number(1230))
print('Ex3: ',reverse_number(1083123))
# another solution

def reverse_number_another(number):
	result = ''
	while number > 0:
		last_num = number % 10
		number = number // 10
		result += f'{last_num} '
	return result


print('Ex3: ',reverse_number_another(1230))
