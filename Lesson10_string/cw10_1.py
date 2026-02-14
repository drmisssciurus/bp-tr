text = "hello world"
text2 = ('hello'
        'world')
text3 = '''hello 
world'''
print(text)
print(text2)
print(text3)

print(text[-0])
print(text[-1])
print(text[0])

print(len(text))

t = '    '
print(len(t))
t = ''
print(len(t))
text_upper = text.upper()
print(text.upper())
print(text.lower())

login = '  sveta  '
print('sveta'==login)

print('sveta'==login.strip())

login = '  sveta malin  '
print('sveta malin'==login)

print('sveta malin'==login.strip())

words = text3.split(' ')
print(words)

text5 = "We, combine, precise, technology, with, practical, farming"
words1 = text5.split(',')
print('1', words1)
count = len(words1) - 1
while count > 0:
	result = words1[count].strip() #words1[6]
	print(result)
	count -= 1
# print(words1[0].strip())

print("12345".isdigit())
print("12345aa".isdigit())
print("asdf".isalpha())
print("asdd1".isalpha())
print("12345aa".isdigit())
print("     ".isspace())
t4 = '11.78'
print(t4.isdigit())


def is_float(t:str)->bool:
	if t.startswith('.') or t.endswith('.'):
		return False
	digits = t.split('.')
	if len(digits) != 2:
		return False
	if not digits[0].isdigit() or not digits[1].isdigit():
		return False
	return True