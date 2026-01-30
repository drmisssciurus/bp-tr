# position arg
from lesson6_params.cw_params_ex import radius


def f(a,b,c,):
	return a*b+c

x,y,z = 1,2,3
res = f(x,y,z)
print(res)

# named args or Keys

res = f(a=x,c=y,b=z)

# default

def greeting(name, greet = 'Hello'):
	print(f'{greet}, {name}')

greeting('Alice', 'hi')
greeting('Bob')



