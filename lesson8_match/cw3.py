from unittest import case


def fan_mode(mode:int)->None:
	if type(mode) != int:
		print('Error: invalid type. Pls enter 0,1,2,3')
		return
	# message = "error: invalid mode. Pls enter 0,1,2,3"

	match mode:
		case 0:
			print('Fan is turning off')
		case 1:
			print('Fan is running at speed 1.')
		case 2:
			print('Fan is running at speed 2.')
		case 3:
			print('Fan is running at speed 3.')
		case _:
			print('error: invalid mode. Pls enter 0,1,2,3')


fan_mode(1)
fan_mode(2)
fan_mode(3)
fan_mode('4')
fan_mode(-4)
fan_mode(0)