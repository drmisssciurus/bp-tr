def time_on_route(pure_time:int, hour:int, city:str, year:int)->int:
	if type(hour) != int or type(pure_time) != int or type(year) != int or type(city) != str:
		print("Error: wrong type please enter correct type")
		return -1
	d_t = delay_time(hour)
	d_o_c = delay_on_city(city)
	d_o_y = delay_on_year(year)
	if pure_time < 0 or d_t < 0 or d_o_c < 0 or d_o_y < 0:
		return -1
	result = pure_time + d_t + d_o_c + d_o_y
	return result

def delay_time(hour:int) -> int:
	if hour < 0 or hour >= 24:
		print("Wrong time")
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

def delay_on_city(city:str)->int:
	match city:
		case "Jerusalem":
			delay = 20
		case "Tel-Aviv":
			delay = 35
		case "Beer-Sheva":
			delay = 15
		case "Haifa":
			delay = 25
		case _:
			print("Error: wrong city")
			delay = -1
	return delay


def delay_on_year(year:int)->int:
	if year < 1950 or year > 2026:
		print("Error: wrong year")
		return -1
	if year <= 1995:
		return 15
	if year <= 2005:
		return 10
	if year <= 2017:
		return 5
	return 0

delay_result = time_on_route(45, 7, "Jerusalem", 2025)
print("Error data" if delay_result < 0 else f"Time on route: {delay_result//60} hours {delay_result%60} minutes")
delay_result = time_on_route('45', 7, "Jerusalem", 2025)
print("Error data" if delay_result < 0 else f"Time on route: {delay_result//60} hours {delay_result%60} minutes")
delay_result = time_on_route(45, '7', "Jerusalem", 2025)
print("Error data" if delay_result < 0 else f"Time on route: {delay_result//60} hours {delay_result%60} minutes")
delay_result = time_on_route(45, 7, "Jeruslem", 2025)
print("Error data" if delay_result < 0 else f"Time on route: {delay_result//60} hours {delay_result%60} minutes")
delay_result = time_on_route(45, 7, "Jerusalem", 1990)
print("Error data" if delay_result < 0 else f"Time on route: {delay_result//60} hours {delay_result%60} minutes")

# guard case
def delay_time_match(hour:int) -> int:
	if hour < 0 or hour >= 24:
		print("Wrong time")
		return -1
	match hour:
		case hour if 7< hour <= 9:
			delay = 20
		case hour if 9< hour <= 11:
			delay = 10
		case hour if 11 < hour <= 13:
			delay = 5
		case _:
			delay = 0
	return delay

