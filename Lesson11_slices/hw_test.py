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