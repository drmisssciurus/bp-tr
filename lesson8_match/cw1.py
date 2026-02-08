def alcohol_pyramid(age:int)->str:
	warning = ''
	if type(age) != int:
		warning ='Error: invalid type'
		return warning
	if age < 0:
		warning ='Error: invalid age'
		return warning
	if age <= 17:
		warning = 'Alcohol not permitted.'
	elif age <= 80:
		warning = 'Alcohol permitted.'
	else: warning = 'Alcohol permitted. But not recommended.'
	return warning

print(alcohol_pyramid('100'))
print(alcohol_pyramid(19))
print(alcohol_pyramid(5))
print(alcohol_pyramid(0))
print(alcohol_pyramid(100))

alcohol_pyramid(-18)


def alcohol_pyramid1(age:int)->str:
	if type(age) != int:
		return f'Error: invalid type{type(age)}'
	if age < 0:
		return f'Error: invalid age {age}'
	if age > 170:
		return f'invalid age {age}.'

	if age<=17:
		message = 'Alcohol not permitted.'
	elif age<=80:
		message = 'Alcohol permitted.'
	else: message = 'Alcohol permitted. But not recommended.'
	return message
