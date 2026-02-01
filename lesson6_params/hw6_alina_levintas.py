"""
divide(a, b)
function should return result of dividing a to b
get a and b values by input()
"""

number_one_for_divide = float(input("Enter first number for divide: "))
number_two_for_divide = float(input("Enter second number for divide: "))


def divide(a, b):
	return a / b


result_divide = divide(number_one_for_divide, number_two_for_divide)
print("Your result for divide is ", result_divide)

print("***************************************")

"""
power (a, b)
should return
power a to b
get a and b values by input()
"""

number_one_for_power = float(input("Enter first number for power: "))
number_two_for_power = float(input("Enter second number for power: "))


def power(a, b):
	return a ** b


result_power = power(number_one_for_power, number_two_for_power)
print("Your result for power is ", result_power)

print("***************************************")

"""
exchange(nis, rate)
calculate amount of dollars by nis and rate of dollar
get nis
and rate values by input()
"""

print("You want to exchange shekels to dollars")
shekels = float(input("Please enter number of shekels: "))
rate_today = float(input("Please enter today rate: "))


def exchange(nis, rate):
	return nis / rate


exchange_result = exchange(shekels, rate_today)
print(f"You will get {exchange_result:.2f} dollars for {shekels} shekels")

print("***************************************")

"""
exchange_adv(nis, rate, commission)
example:
nis = 100
rate = 4
commission = 2%
get nis, rate and commission values by input()
"""
print("Grate! Unfortunately we have a commission :)")
today_commission = float(input("Enter today commission: "))

commission_amount = shekels * (today_commission / 100)

def exchange_adv(nis, rate, commission):
	count_commission_amount = shekels * (today_commission / 100)
	shekels_after_commission = shekels - count_commission_amount

	return shekels_after_commission / rate

exchange_adv_exchange_result = exchange_adv(shekels, rate_today, today_commission)
print(f"You will get {exchange_adv_exchange_result:.2f} dollars for {shekels} after comission")

print("***************************************")

"""
Salary Calculation (Netto) => function with parameters
"""

print("Now we will count your salary netto")

hours = float(input("Please enter hours: "))
wage = float(input("Please enter wage: "))
tax = float(input("Please enter tax: "))
name = input("Please enter your name: ")

def salary(hours_, wage_, tax_):
	salary_brutto = hours_ * wage_
	salary_netto = salary_brutto - (salary_brutto * (tax_ / 100))
	return salary_netto

salary_result = salary(hours, wage, tax)
print(f"{name} will get {salary_result:.2f} shekels for {hours} hours")