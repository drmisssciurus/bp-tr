from Lesson16_OOP_inheritance.cw16_1 import Product


class MilkProduct(Product):
	def __init__(self, name:str, price:int, unit:str, code:str, kosher:bool, milk_type:str):
		super().__init__(name, price, unit, code, kosher)
		self.__milk_type = milk_type

	def __str__(self):
		return super().__str__() + f" milk type: {self.__milk_type}"

	def set_milk_type(self, milk_type):
		self.__milk_type = milk_type

	def get_milk_type(self):
		return self.__milk_type
