class Person:
	def __init__(self, name:str, age:int, id:int, location:str):
		self.name = name
		self.age = age
		self.id = id
		self.location = location

	def __str__(self):
		to_print = (f"name: {self.name} age: {self.age}, id: {self.id}, location: {self.location}")
		return to_print

	def greet(self):
		print(f"Hello, {self.name}")

p1 = Person("name", 23, 34, "telaviv")
# p2 = Person("name")
print(p1)
p1.greet()

"""
Car Class
model
year
color
str->print
============
drives straight
turns right
turns left
stops
car shop-> 5 objects


Class Book
title
author
pages
str->print


create 5 objects types Book
library - storage for books
print all books from library
"""
