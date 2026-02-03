"""
if condition: (=>true)
	code if conditional is true
if false code would continue here
"""

a = 10
if a>5:
	print(a)
print("no hehe")

def divide(a,b):
	if b==0:
		return "division by zero not allowed"
	return a/b

print(divide(10,0))

def divide1(a,b):
	if b!=0:
		return a/b
	return "division by zero not allowed"

print(divide1(10,1))
