#-*- encoding: utf-8 -*-

# Error
#def func():

def func():
	pass


def func(num, num1=1, num2=2):
	print(num, num1, num2)

func(1, 3, 4) # 1 3 4

func(5) # 5 1 2

# Error
#func()

def func(**args):
	for k, v in args.items():
		print('key: ' + k, 'value: ' + v)
	for k in args.keys():
		print('key: ' + k, 'value: ' + args[k])

func(name = "rxb", age = "24")


def func(name, age):
	print('name: ' + name, 'age: ' + age)

people = {"name": "rxb", "age": "24"}
func(**people) # name: rxb age: 24

def func(num, *args):
	print(num)
	for a in args:
		print(a)

func(1, 2, 3, 4, 5, 6)

def func(num, num1):
	print(num, num1)

func(num1 = 2, num = 1) # 1 2

d = {
	"num": 3,
	"num1": 4
}

func(**d) # 3 4

t = (4, 5)
func(*t) # 4 5

def func():
	'''
		The documentation of the func
	'''
	print("func")

print(func.__doc__)

l = lambda num1, num2: num1 + num2
print(l(2, 3)) # 5
