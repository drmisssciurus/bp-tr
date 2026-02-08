def check_position(name:str)->str:
	if type(name) != str:
		return f"Error: invalid type {type(name)}. Pls enter string"
	res = ''
	match name:
		case "Roman":
			res = 'Developer'
		case "Alina":
			res = 'Engineer'
		case "Rivka":
			res = 'Accounter'
		case _:
			res = "Unknown person"
	return f'{name} is {res}'

print(check_position("Roman"))
print(check_position("Alina"))
print(check_position("Rivka"))
print(check_position("Alla"))
print(check_position(None))
print(check_position(1))
