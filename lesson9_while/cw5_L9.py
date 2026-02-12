import random

target = random.randint(1,20)
guess = 0

while guess != target:
	guess = int(input("Guess a number between 1 and 20: "))
	if guess < target:
		print("Too low")
	elif guess > target:
		print("Too high")
	else:
		print("Correct")
		break