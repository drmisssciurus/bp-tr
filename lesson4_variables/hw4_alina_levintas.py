# 1. You enter the number of shekels and the dollar exchange rate. The console displays the number of dollars you can buy, accurate to the second digit.

def exchange():
	shekels = float(input('enter the number of shekels: '))
	dollar_exchange_rate = float(input('enter the dollar exchange rate: '))
	exchange_result = shekels * dollar_exchange_rate
	print(f"For {shekels} shekels you can buy {exchange_result:.2f} dollars")

# exchange()

# 2. You enter the cost of your purchase and the amount of money you give to the cashier. The change is displayed on the console.

def change():
	purchase_summ = float(input('Enter the number of cost of your purchases: '))
	money_given = float(input('Enter amount of money you give to the cashier: '))
	change_result = money_given - purchase_summ
	print(f"Your change is {change_result}₪")

# change()

# 3. You enter the number of hours worked, the cost of an hour and tax. your net salary (minus tax) is displayed on the console.

def salary_counter():
	hour_cost = float(input('Enter your hour cost: '))
	hours_worked = float(input('Enter your hours worked in this month: '))
	tax = float(input('Enter your tax: '))
	salary_brutto = hour_cost * hours_worked
	salary_netto = salary_brutto - (salary_brutto * (tax / 100))
	print(f"Your salary in this month is: brutto ₪{salary_brutto:.2f}; netto ₪{salary_netto:.2f}")

salary_counter()