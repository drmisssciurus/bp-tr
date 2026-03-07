from Lesson16_OOP_inheritance.cw16_3 import MilkProduct
from cw16_1 import Product

p1 = Product("mango", 13, "250 g", "654yuk654", True)
p2 = Product("yogurt", 2.3, "250 ml", "654wf654", True)

mini_market = [p1,p2]
for p in mini_market:
	print(p)

# инкапсуляция способ скрыть поля класса от внешнего присутствия,
# сейчас мы можем обратится к любому полю и поменять его
# для этого надо писать __ перед атрибутом обьекта

p1.price = -100
for p in mini_market:
	print(p)

print(p1.get_name())
p1.set_name("Milk")
print(p1.get_name())

p1.set_price(100)
print(p1.get_price())

# наследование
m1 = MilkProduct("yougurt", 4,'1', '23', True, "yoyoy ")
print(m1)

# мульти наследование
