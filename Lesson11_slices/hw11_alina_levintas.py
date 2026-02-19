# Задача 1 Проверка на палиндром
# Условие
# Напишите функцию, которая получает строку и возвращает True,
# если строка является палиндромом, и False в противном случае.
# Палиндром
# Использовать нужно срез строки, а не цикл.

def if_palindrome(text:str)->bool:
	if type(text) != str:
		print('Error: type not str')
		return False
	if text.lower() == text[::-1].lower():
		return True
	return False

print(if_palindrome('Alina'))
print(if_palindrome('Stats'))
print(if_palindrome('palindrome'))

# Задача 2 Удалить первый и последний символ
# Условие
# Напишите функцию, которая получает строку и возвращает новую строку без
# первого и последнего символа.
# Если длина строки меньше 2 — вернуть пустую строку

def del_first_last(text:str)->str:
	if len(text) < 2:
		return ''
	new_text = text.strip()
	return new_text[1:len(new_text)-1]

print(del_first_last(' e4 '))
print(del_first_last('stanislav'))

# Задача 3 Поменять местами половины строки
# Условие
# Напишите функцию, которая получает строку чётной длины и меняет её половины
# местами.
# Если длина нечётная вернуть строку без изменений.

def switch_text(text:str)->str:
	if len(text) % 2 != 0:
		return text
	text_len = len(text)
	i = int(text_len / 2)
	return  text[i:] + text[:i]


print(switch_text('AlinaStats'))
print(switch_text('StatsAlina'))
print(switch_text('palindromeq'))