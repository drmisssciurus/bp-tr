"""
while conditions:
"""

# a = 10
# while True:
# 	print(a)
# 	a+=1
# 	if a >= 10:
# 		break

def password():
	passw = 'qwerty'
	count = 0
	while True:
		print(count)
		attempt = input('Insert pass: ')
		if attempt == passw:
			print('good')
			return
		if count == 3:
			print('no attempts')
			return
		count+=1


def password():
	pass_ = "qwerty"# 3 attempt
	max_att = 3
	count=0
	
	while True:
		attempt = input(f"insert pass, you have {max_att - count} attempts left >>>")
		count+=1
		if attempt==pass_ or count >= max_att:
			return "hello " if attempt==pass_ else "try later"

print(password())


