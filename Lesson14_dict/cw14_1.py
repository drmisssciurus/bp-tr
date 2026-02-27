# list -> elements
# tuple -> elements
from calendar import month

t1 = ([1,2,3], [2,3,4])
t1[0][0] = 100
print(t1)
print(t1[0])
print(t1[1])

t1[1][0] = 100
print(t1)
t1[0].append(1000)
print(t1)


# set-> unique elements
# dict -> key-value

months = {
	"Jan":1,
	"Feb":2,
	"Match":3,
	"April":4
}

print(months["Jan"])

d={}
d2=dict()

user = {
	"name": "Anna",
	"age": 25,
	"city": "Haifa"
}

print(user)

user1 = dict(name="Alina", age=23)
print(user1)

print(months.get("May")) #safe use

for key in months.keys():
	print(key, end='-')
print()
for value in months.values():
	print(value, end='-')

for key, values in months.items():
	print(key, '->>>', values)

for key, value in months.items():
	print(key, "->", value)
months["new"] = 123
# for k in months:
# 	if k == "Jan":
# 		months["new1"] = 123

user1['city'] = "kfarsaba"
print(user1)
