def check_num(number):
	if number < 0:
		return	"number is negative"
	if number == 0:
		return "number is zero"
	return "number is positive"
num_inp = float(input("Please enter any number: "))

print(check_num(num_inp))