#raise
age = -5
def check_age(age):
	if age < 0:
		raise ValueError('age cannot be negative')
	else:
		print("correct")
check_age(age)