class Product:
	def __init__(self, name:str, price:float, unit:str, code:int, kosher:bool):
		self._name = ''
		self._price = 0.
		self._unit = ''
		self._code = 0
		self._kosher = False

		self.set_name(name)
		self.set_price(price)
		self.set_unit(unit)
		self.set_code(code)
		self.set_kosher(kosher)

	def get_name(self):
		return self._name
	def get_price(self):
		return self._price
	def get_unit(self):
		return self._unit
	def get_code(self):
		return self._code
	def get_kosher(self):
		return self._kosher

	def set_name(self, name):
		if isinstance(name, str) and name.strip():
			self._name = name
		else:
			print("Invalid name")

	def set_unit(self, unit):
		if isinstance(unit, str) and unit.strip():
			self._unit = unit
		else:
			print("Invalid unit")

	def set_code(self, code):
		if isinstance(code, int) and code < 0:
			self._code = code
		else:
			print("Invalid code")

	def set_kosher(self, kosher):
		if isinstance(kosher, bool):
			self._kosher = kosher
		else:
			print("Invalid kosher")

	def set_price(self, price):
		if isinstance(price, float) and price < 0:
			self._price = price
		else:
			print("Invalid price")

# isinstance vs type

	def __str__(self):
		return (f"name: {self._name}| price: {self._price}|"
		        f"unit: {self._unit}| code: {self._code}|"
		        f"kosher: {self._kosher}")

	def __repr__(self):
		return (f"name: {self._name}, price: {self._price},"
		        f"unit: {self._unit}, code: {self._code},"
		        f"kosher: {self._kosher}")

class MilkProduct(Product):
	def __init__(self, name:str, price:float, unit:str, code:int, kosher:bool, milk_type:str):
		super().__init__(name, price, unit, code, kosher)
		self._milk_type = ""
		self.set_milk_type(milk_type)

	def set_milk_type(self, milk_type):
		if isinstance(milk_type, str) and milk_type.strip():
			self._milk_type = milk_type
		else:
			print("Invalid milk type")

	def get_milk_type(self):
		return self._milk_type

	def __str__(self):
		return f"Milk Product -> {super().__str__()}, milk type: {self._milk_type}"

	def __repr__(self):
		return (f"Milk Product(name: {self._name}, price: {self._price},"
		        f"unit: {self._unit}, code: {self._code},"
		        f"kosher: {self._kosher}, milk type: {self._milk_type})")

class MeatProduct(Product):
	def __init__(self, name:str, price:float, unit:str, code:int, kosher:bool, meat_type:str):
		super().__init__(name, price, unit, code, kosher)
		self._meat_type = ""
		self.set_meat_type(meat_type)

	def set_meat_type(self, meat_type):
		if isinstance(meat_type, str) and meat_type.strip():
			self._meat_type = meat_type
		else:
			print("Invalid meat type")

	def get_meat_type(self):
		return self._meat_type

	def __str__(self):
		return f"meat Product -> {super().__str__()}, meat type: {self._meat_type}"

	def __repr__(self):
		return (f"meat Product(name: {self._name}, price: {self._price},"
		        f"unit: {self._unit}, code: {self._code},"
		        f"kosher: {self._kosher}, meat type: {self._meat_type})")

class BreadProduct(Product):
	def __init__(self, name:str, price:float, unit:str, code:int, kosher:bool, gluten:str):
		super().__init__(name, price, unit, code, kosher)
		self._gluten = ""
		self.set_gluten(gluten)

	def set_gluten(self, gluten):
		if isinstance(gluten, str) and gluten.strip():
			self._gluten = gluten
		else:
			print("Invalid gluten")

	def get_gluten(self):
		return self._gluten

	def __str__(self):
		return f"Bread Product -> {super().__str__()} | gluten: {self._gluten}"

	def __repr__(self):
		return (f"Bread Product(name: {self._name}, price: {self._price},"
		        f"unit: {self._unit}, code: {self._code},"
		        f"kosher: {self._kosher}, gluten: {self._gluten})")

product1 = MilkProduct("Milk 3%", 8, "bottle", 123, True, "cow")
product2 = MilkProduct("Goat Yogurt", 12, "cup", 34245, True, "goat")
product3 = MilkProduct("Cheese", 25, "pack", 4654, True, "cow")
product4 = MeatProduct("Chicken Breast", 35, "kg", 234, True, "chicken")
product5 = MeatProduct("Beef Steak", 70, "kg", 4234, True, "beef")
product6 = MeatProduct("Turkey Mince", 42, "kg", 345, True, "turkey")
product7 = BreadProduct("White Bread", 10, "loaf", 867, True, True)
product8 = BreadProduct("Gluten Free Bread", 18, "loaf", 453, True, False)
product9 = BreadProduct("Baguette", 9, "pcs", 34, True, True)
product10 = BreadProduct("Rye Bread", 11, "loaf", 45346, True, True)

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