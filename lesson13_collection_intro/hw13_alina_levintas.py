array = [7, 4,-3, 9, 7, 6]

# 1. Функция получает list и возвращает сумму нечётных.
# Пример: [7, 4,-3, 9, 7, 6] → сумма нечётных 7 + (-3) + 9 + 7 = 20

def get_odd_summ(some_arr)->int:
	res = 0
	for item in some_arr:
		if item % 2 != 0:
			res += item
	return res

print(get_odd_summ(array))

# Тоже самое, но нечетных по индексу элементов

def get_odd_position_summ(some_arr)->int:
	res = 0
	len_arr = len(some_arr)
	for item in range(0,len_arr):
		if item % 2 != 0:
			res += some_arr[item]
	return res

print(get_odd_position_summ(array))

# Функция получает list и возвращает максимальный элемент.

def return_max_elem(some_arr)->int:
	max_elem = some_arr[0]
	for x in some_arr:
		if x > max_elem:
			max_elem = x
	return max_elem

print(return_max_elem(array))

# Функция получае list и печатает чётные элементы с конца в начало.

def print_even_from_ent_to_start(some_arr)->None:
	len_arr = len(some_arr)
	while len_arr > 0:
		if some_arr[len_arr-1] % 2 == 0:
			print(some_arr[len_arr-1], end= " ")
		len_arr -= 1

print_even_from_ent_to_start(array)

# Функция получает две строки и возвращает индекс, с которого вторая строка начинается в первой.

def return_start_index(text, sub)->str:
	result = f'\nSubstring start on index {text.find(sub)}'
	return result

print(return_start_index('asdf', 'df'))