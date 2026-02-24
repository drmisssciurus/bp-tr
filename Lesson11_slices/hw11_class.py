 # == > < >= <= != ----> true or false
print(5==5)
print(5==6)
print("abcd"=="dcba")
print("abcd"=="abcd")

def palindrome(text:str)->bool:
	if type(text) != str:
		print('Error: type not str')
		return False
	# print(text)
	# print(text[::-1])
	# temp = text.strip().split(' ')
	# print(temp)
	# text = ''.join(temp)
	# print(text)
	text = text.replace(" ", "")
	return text.lower() == text[::-1].lower()

print(palindrome('A l i l a'))


def ret_str(text:str)->str:
	if type(text) != str:
		return 'Error: type not str'
	return '' if len(text) <= 2 else text[1:-1]

def switch_str(text:str)->str:
	if type(text) != str:
		return 'Error: type not str'
	if len(text) % 2 != 0:
		return text

	i = len(text) // 2
	return  text[i:] + text[:i]

print(switch_str('qwerty'))