# Задача 1. Количество вхождений «подчисла» (has_subnumber)

def has_subnumber(number:int, sub:int)->int:
	if number < 0 or sub < 0:
		return -1

	new_num = str(number)
	new_sub = str(sub)
	count = 0
	for i in range(0,len(new_num)):
		if new_num[i:i + len(new_sub)] == new_sub:
			count += 1
	return count

print(has_subnumber(34534634, 34))
print(has_subnumber(1111, 11))
print(has_subnumber(123456, 78))

# Задача 2. Сколько раз цифра встречается на всём диапазоне

def count_digit_in_range(n: int, d: int) -> int:
	if type(n) != int or n < 0 or d < 0 or d > 9:
		return -1
	count = 0
	for i in range(0, n + 1):
		s = str(i)
		for ch in s:
			if ch == str(d):
				count += 1
	return count

print(count_digit_in_range(15, 1))


# Задача 3. Заменить все вхождения подчисла на другое

def replace_subnumber(number: int, sub: int, rep: int) -> int:
	if number < 0 or sub < 0 or rep < 0:
		return -1

	new_num = str(number)
	new_sub = str(sub)
	new_rep = str(rep)
	rep_num = ''
	for i in range(0,len(new_num)):
		print('1',i)
		print('1.1', new_num[i:i + len(new_sub)])
		if new_num[i:i + len(new_sub)] == new_sub:
			print('2',new_num[i:i+len(new_sub)])
			replaced_part = new_num[i:i+len(new_sub)].replace(new_sub, new_rep)
			rep_num += replaced_part
			print('3', rep_num)

			continue
		rep_num += new_num[i:i + len(new_sub)]
		print('4',rep_num)

	return int(rep_num)

print(replace_subnumber(34534634, 34, 99))
print(replace_subnumber(1111, 11,2))