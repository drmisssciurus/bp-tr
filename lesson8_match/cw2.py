from pyexpat.errors import messages


def fan_mode(mode:int)->None:
	if type(mode) != int:
		print('Error: invalid type. Pls enter 0,1,2,3')
		return
	message = "error: invalid mode. Pls enter 0,1,2,3"

	if mode == 0:
		message = 'Fan is running at speed 0.'
	elif mode == 1:
		message = 'Fan is running at speed 1.'
	elif mode == 2:
		message = 'Fan is running at speed 2.'
	elif mode == 3:
		message = 'Fan is running at speed 3.'
	print(message)

fan_mode(1)
fan_mode(2)
fan_mode(3)
fan_mode('4')
fan_mode(-4)
