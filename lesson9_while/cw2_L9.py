x = 10
# while x > 0:
# 	print(x, end="")
# 	x+=1

	# infinite cycle

while x > 0:
	print(x, end="")
	x+=1
	if x > 100:
		break

print('\n game over')

def strange_dev(x):
	while x > 0:
		print(x, end="")
		x += 1
		if x > 100:
			return

	print('\n game over dev')

def strange_dev1(x):
	while x > 0:
		print(x, end="")
		x += 1
		if x > 100:
			break

	print('\n game over dev1')

strange_dev(x)
strange_dev1(x)


