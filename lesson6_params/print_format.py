name = "Alice"
age = 25
print('My name is', name, "and my age is", age, "years old")
print('My name is ' + name + " and my age is " + str(age) + " years old")
print(f"My name is {name} and my age is {age} years old")
print("My name is {} and my age is {} years old".format(name, age))
print("My name is %s and my age is %s years old"%(name, age))
# %s - string; %d - integer; %f - float; %c - char
print("My name is {n} and my age is {a} years old".format(n=name, a=age))
# 12345 = 1.2345*10**4 (1.2345 - это мантиса): 
