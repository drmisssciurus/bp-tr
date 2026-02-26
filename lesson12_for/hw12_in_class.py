def has_subnumber(number:int, sub:int)->int:
	if type(number) != int or type(sub) != int:
		return -1
	if number < 0 or sub < 0:
		return -1

	s_num = str(number)
	s_sub = str(sub)
	count = 0
	sub_len = len(s_sub)
	num_len = len(s_num)

	if sub_len > num_len:
		return 0

	#123456 4567 (index 6-4+1) we will go just to 2 index 3 position
	print(num_len - sub_len + 1)
	for i in range(0, num_len - sub_len + 1):
		print('i: ', i)
		if s_num[i:i+sub_len] == s_sub:
			count +=1
	return count

# print(has_subnumber(123456, 4567))
# print(has_subnumber(123412341235, 123))

"""
1234567 4567
12134567 -> 4 >>> if we find 4 we take 5
"""

def count_digit_in_range(n: int, d: int) -> int:
	if type(n) != int or type(d) != int:
		return -1
	if n < 0 or d < 0 or d > 9:
		return -1

	target = str(d)
	count = 0

	for i in range(n + 1):
		for ch in str(i):
			if ch == target:
				count += 1
	return count

# print(count_digit_in_range(100, 1))

def replace_subnumber(number: int, sub: int, rep: int) -> int:
	if type(number) != int or type(sub) != int or type(rep) != int:
		return -1
	if number < 0 or sub < 0 or rep < 0:
		return -1


	s_num = str(number)
	s_sub = str(sub)
	s_rep = str(rep)

	# result = ''
	# i = 0
	# sub_len = len(s_sub)
	#
	# while i < len(s_num):
	# 	if s_num[i:i+sub_len] == s_sub:
	# 		result += s_rep
	# 		i += sub_len
	# 	else:
	# 		result+=s_num[i]
	# 		i+=1
	# return int(result)
	return int(s_num.replace(s_sub,s_rep))

# print(replace_subnumber(34534634, 34, 99))

def normalize_spaces(text: str)-> str:
	if not isinstance(text, str):
		error = 'Errorooorrr type'
		return error
	print(text.split())
	return ' '.join((text.split()))


# print(normalize_spaces('       f   g e t h '))

def are_anagrams(s1:str, s2:str)->bool:
	if not isinstance(s1, str) or not isinstance(s2, str):
		return False
	s1_n = s1.lower().replace(' ', '')
	s2_n = s2.lower().replace(' ', '')

	for ch in s2_n:
		pos = s1_n.find(ch)
		if pos == -1:
			return False
		s1_n = s1_n[:pos] + s1_n[pos+1:]
	return True

print(are_anagrams( "Tom Marvolo Riddle" , "I am Lord Voldemort"))