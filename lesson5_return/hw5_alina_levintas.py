#### Task 1: Apple Collection and Calculation ###

def haim():
	haim_apples = float(input("How many apples Haim has in kilograms?>>> "))
	return haim_apples

def nastya():
	nastya_apples = float(input("How many apples Nastya has in kilograms?>>> "))
	return nastya_apples

def alex():
	alex_apples = float(input("How many apples Alex has in kilograms?>>> "))
	return alex_apples

def anna():
	anna_apples = float(input("How many apples Anna has in kilograms?>>> "))
	return anna_apples

total_apples_kilo = haim() + nastya() + alex() + anna()
number_of_members = 4
average_for_each_member_family = total_apples_kilo / number_of_members

print(f"Total apples in family {total_apples_kilo} kg. Average for each is {average_for_each_member_family:.2f} kg")

#### Task 2: Salary Calculation (Netto) ####

def salary():
	hours = float(input("Please enter hours: "))
	wage = float(input("Please enter wage: "))
	tax = float(input("Please enter tax: "))
	salary_brutto = hours * wage
	salary_netto = salary_brutto - (salary_brutto * (tax / 100))
	print(f"Netto salary is {salary_netto:.2f}")

def person_salary():
	print("Enter Alex's numbers for calculating his salary:")
	salary()
	print("Enter Nastya's salary for calculating her salary")
	salary()

person_salary()


#### Task 3: Advanced Salary Calculation (with Bonus) ####

def salary_adv():
	hours = float(input("Please enter hours: "))
	wage = float(input("Please enter wage: "))
	tax = float(input("Please enter tax: "))
	bonus = float(input("Please enter bonus: "))
	salary_brutto = hours * wage
	salary_netto = salary_brutto - (salary_brutto * (tax / 100))
	salary_bonus = salary_brutto * (bonus/100)
	print(f"Netto salary is {salary_netto:.2f} and your bonus is {salary_bonus:.2f}")

def person_salary_with_bonus():
	print('Enter Alex\'s numbers for calculating his salary with bonus:')
	salary_adv()
	print('Enter Nastya\'s salary for calculating her salary with bonus:')
	salary_adv()

person_salary_with_bonus()