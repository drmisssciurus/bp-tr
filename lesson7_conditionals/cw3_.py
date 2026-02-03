def sleep_or_not(sleep_time):
	if sleep_time < 0 or sleep_time > 24:
		print("wrong time")
		return
	if 7 < sleep_time < 22:
		print("im not sleeping")
		return
	print("im sleeping")
	return



sleep_or_not(-5)
sleep_or_not(8)
sleep_or_not(21)
sleep_or_not(56)
sleep_or_not(0)
sleep_or_not(1)
sleep_or_not(-2)
sleep_or_not(25)
sleep_or_not(23)

