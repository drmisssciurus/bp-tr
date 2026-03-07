class Bird:
	def __init__(self, name):
		self.name = name

	def eat(self):
		print(f"{self.name} is eating")

class Flying:
	def fly(self):
		print("i can fly")

class Swimming:
	def swim(self):
		print("i can swim")

class Duck(Bird, Flying, Swimming):
	def quack(self):
		print("i can quack")

class Seagull(Bird, Flying):
	def cry(self):
		print("i can cry")

duck = Duck('Donald')
print("Duck " + duck.name)
duck.quack()
duck.eat()
duck.swim()
duck.fly()

seagull = Seagull('Seagullarria')
print("Seagull " + seagull.name)
seagull.eat()
seagull.cry()


