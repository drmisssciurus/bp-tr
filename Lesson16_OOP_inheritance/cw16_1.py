class Product:
	def __init__(self, name:str, price:int, unit:str, code:str, kosher:bool): # параметры обьекта
		if isinstance(name, str):
			self.__name = name  #  атрибуты
		else: self.__name = "No name"
		self.__price = price
		self.__unit = unit
		self.__code = code
		self.__kosher = kosher

	def __str__(self):
		return f"{self.__name}, {self.__price}, {self.__unit}, {self.__code}, {self.__kosher}"

	# геткрры и сеттеры

	def set_name(self, name):
		self.__name = name

	def get_name(self):
		return self.__name

	def set_price(self, price):
		if price < 0:
			return
		self.__price = price

	def get_price(self):
		return self.__price

	# def update_product(self, name, .....):
	# 	if isinstance(name, str):
	# 		self.__name = name
	# 	self.__price = price
	# 	self.__unit = unit
	# 	self.__code = code
	# 	self.__kosher = kosher