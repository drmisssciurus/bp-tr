
def delay_time(hour: int)->int or str:
	if type(hour) != int:
		return -1
	if 7 < hour <= 9:
		delay = 20
	elif 9 < hour < 11:
		delay = 10
	elif 11 <= hour < 13:
		delay = 5
	else:
		delay = 0
	return delay


def delay_on_city(city:int)->str or int:
	if type(city) != int:
		return -1
	match city:
		# "Jerusalem"
		case 1:
			delay = 20
		# "Tel-Aviv"
		case 2:
			delay = 35
		# "Beer-Sheva"
		case 3:
			delay = 15
		# "Haifa"
		case 4:
			delay = 25
		case _:
			return -1
	return delay


def delay_on_year(year):
	if year <= 1995:
		delay = 15
	elif 1996 < year <= 2005:
		delay = 10
	elif year <= 2017:
		delay = 5
	elif year <= 2024:
		delay = 0
	else:
		return -1
	return delay

def time_on_route(pure_time, hour, city, year):
	if type(hour) != int or type(city) != int or type(pure_time) != int or type(year) != int:
		error = "Error: wrong type please enter correct type - number"
		return error
	if hour > 23:
		error = "Error: wrong time, time cannot be more than 23"
		return error
	which_hour = delay_time(hour)
	which_city = delay_on_city(city)
	which_year = delay_on_year(year)
	if which_hour < 0 or which_city < 0 or which_year < 0:
		error = "Error"
		return error
	res = pure_time + which_hour + which_city + which_year
	return res

print(time_on_route(100,11,1, 2000))
print(time_on_route(1,11,1, 2000))

print(time_on_route(100,'11',1, 2000))
print(time_on_route(1,11,'5', 2000))
print(time_on_route('1',11,'5', 2000))
print(time_on_route(1,31,1, 2000))
print(time_on_route(1,11,1, 3000))
print(time_on_route(1,11,6, 3000))



	# hours = res//60
	# minutes = res - (hours * 60)
	# if res >= 60:
	# 	return f"The road will take {hours} hours and {minutes} minutes"
	# return f"The road will take {res} minutes"
