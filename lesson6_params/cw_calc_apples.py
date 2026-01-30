def calculate_apples(name):
	print(name, end="")
	apples = input(", enter amount of apples: ")

	return float(apples), 1

b0, c0 = calculate_apples('Bob')
b1, c1 = calculate_apples('Alice')
b2, c2 = calculate_apples('Ale')
b3, c3 = calculate_apples('Alice')

print(f"average apples: {(b0 + b1 + b2 + b3)/(c0 + c1 + c2 + c3)} and total {b0+b1+b2+b3}")