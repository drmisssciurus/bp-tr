# Задача 3. Заменить все вхождения подчисла на другое
# Чуть посложнее, если захочешь «звёздочку».
#
# Условие
# Даны три неотрицательных числа:
# number, sub, rep.
#
# Нужно заменить все вхождения «подчисла» sub в числе number на число rep и вернуть новое число.
#
# def replace_subnumber(number: int, sub: int, rep: int) -> int:
# ...
#
# Примеры:
#
#  number = 34534634, sub = 34, rep = 99
# 34534634 → 99 5 99 6 99 →
# результат 99599699.
#
#  number = 1111, sub = 11, rep = 2
# "1111" → "22" (две замены 11 → 2).


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