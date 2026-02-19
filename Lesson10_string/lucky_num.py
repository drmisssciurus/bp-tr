# Task 3: Lucky Number

def is_lucky_number_sides(number:int)->str:
	count_for_length = 0
	temp = number
	while temp != 0:
		count_for_length += 1
		temp = temp// 10
	if count_for_length % 2 != 0:
		error = 'error: number should have equal number of numbers for both sides'
		return error

	sum1 = 0
	new_count_sum1 = count_for_length / 2
	while new_count_sum1 > 0:
		sum1 = number%10 + sum1
		new_count_sum1-=1
		number//=10

	sum2 = 0
	new_count_sum2 = count_for_length / 2
	while new_count_sum2 > 0:
		sum2 = number%10 + sum2
		new_count_sum2-=1
		number//=10

	if sum1 == sum2:
		return 'luck'
	return 'not luck'


print(is_lucky_number_sides(12344321))
print(is_lucky_number_sides(123442321))
print(is_lucky_number_sides(122334423521))
