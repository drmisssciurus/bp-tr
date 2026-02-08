def fan(mode:int)->None:
	if type(mode) != int:
		print('Error: invalid mode')
		return
	if mode == 0:
		print('Fan is off')
		return
	if mode == 1:
		print('Fan is running at speed 1.')
		return
	if mode == 2:
		print('Fan is running at speed 2.')
		return
	if mode == 3:
		print('Fan is running at speed 3.')
		return
	print('Error: invalid mode. Pls enter 0,1,2,3')