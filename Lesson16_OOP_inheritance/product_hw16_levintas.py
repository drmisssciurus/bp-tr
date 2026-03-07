class Product:
	def __init__(self, name: str, price: int, unit: str, code: str, kosher: bool):
		if isinstance(name, str):
			self.__name = name
		else:
			self.__name = "No name"
		self.__price = price
		self.__unit = unit
		self.__code = code
		self.__kosher = kosher


	def __str__(self):
		return f"{self.__name}, {self.__price}, {self.__unit}, {self.__code}, {self.__kosher}"


	def set_name(self, name):
		self.__name = name

	def get_name(self):
		return self.__name

	def set_price(self, price):
		if isinstance(price, int) or price < 0:
			self.__price = "Error price"
		else: self.__price = price

	def get_price(self):
		return self.__price

class MilkProduct(Product):
	def __init__(self, name: str, price: int, unit: str, code: str, kosher: bool, milk_type: str):
		super().__init__(name, price, unit, code, kosher)
		self.__milk_type = milk_type

	def __str__(self):
		return super().__str__() + f" milk type: {self.__milk_type}"

	def set_milk_type(self, milk_type):
		if isinstance(milk_type, str):
			self.__milk_type = milk_type
		else:
			self.__milk_type = "Milk type not found"

	def get_milk_type(self):
		return self.__milk_type


class MeatProduct(Product):
	def __init__(self, name: str, price: int, unit: str, code: str, kosher: bool, meat_type: str):
		super().__init__(name, price, unit, code, kosher)
		self.__meat_type = meat_type

	def __str__(self):
		return super().__str__() + f" Meat type: {self.__meat_type}"

	def set_meat_type(self, meat_type):
		if isinstance(meat_type, str):
			self.__meat_type = meat_type
		else:
			self.__meat_type = "Meat type not found"

	def get_meat_type(self):
		return self.__meat_type


class BreadProduct(Product):
	def __init__(self, name: str, price: int, unit: str, code: str, kosher: bool, gluten: bool):
		super().__init__(name, price, unit, code, kosher)
		self.__gluten = gluten

	def __str__(self):
		return super().__str__() + f"  Gluten: {self.__gluten}"

	def set_gluten(self, gluten):
		if isinstance(gluten, bool):
			self.__gluten = gluten
		else:
			self.__gluten = False

	def get_gluten(self):
		return self.__gluten

product1 = MilkProduct("Milk 3%", 8, "bottle", "M001", True, "cow")
product2 = MilkProduct("Goat Yogurt", 12, "cup", "M002", True, "goat")
product3 = MilkProduct("Cheese", 25, "pack", "M003", True, "cow")
product4 = MeatProduct("Chicken Breast", 35, "kg", "ME001", True, "chicken")
product5 = MeatProduct("Beef Steak", 70, "kg", "ME002", True, "beef")
product6 = MeatProduct("Turkey Mince", 42, "kg", "ME003", True, "turkey")
product7 = BreadProduct("White Bread", 10, "loaf", "B001", True, True)
product8 = BreadProduct("Gluten Free Bread", 18, "loaf", "B002", True, False)
product9 = BreadProduct("Baguette", 9, "pcs", "B003", True, True)
product10 = BreadProduct("Rye Bread", 11, "loaf", "B004", True, True)

mini_market = [
    product1,
    product2,
    product3,
    product4,
    product5,
    product6,
    product7,
    product8,
    product9,
    product10
]

for product in mini_market:
	print(product)