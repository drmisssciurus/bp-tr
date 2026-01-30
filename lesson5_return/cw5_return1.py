def greeting():
	print('Hello')

# result = greeting()

print(result) #ничего не возращает

def greeting():
	return "Hello"

result = greeting()

print(result) #а так возращает

def milk():
	product = float(input("Pls enter milk price for 1 pack: "))
	quantity = float(input("Pls enter quantity of milk: "))
	return product * quantity

def meat():
	product = float(input("Pls enter milk price for 1 kilogram: "))
	quantity = float(input("Pls enter quantity of kilogram: "))
	return product * quantity

def bread():
	product = float(input("Pls enter milk price for 1: "))
	quantity = float(input("Pls enter quantity of bread: "))
	return product * quantity

total_price = milk()
print(total_price)
total_price+=bread()
print(total_price)
total_price+=meat()
print('_____________________________')
print(f'Total price of your product is {total_price}')


