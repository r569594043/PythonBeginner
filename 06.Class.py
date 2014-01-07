#-#- encoding: utf-8 -#-

class Animal():
	"""Animal Class"""

	name = "Animal"

	def __init__(self):
		self.className = 'Animal'

# Inherit

class Cat(Animal):
	"""Cat Class"""
	name = 'Cat'

	def __init__(self, name):
		super(Animal, self).__init__()
		self.className = 'Cat'
		self.name = name
	def shout(self):
		print(self.name + ' shout: miao~')
	def favorite(self):
		print('my favorite food is fish')


class Dog(Animal):
	"""Dog Class"""
	def __init__(self):
		super(Animal, self).__init__()
		self.className = 'Dog'
	def shout(self):
		print(self.name + ' shout: wang~')
	def power(self):
		print('my super power is watch your house')



kitty = Cat('kitty')
kitty.shout()
print(kitty.name)
print(Cat.name)
print(Animal.name)

wangcai = Dog()
# dog.name = 'wangcai'
Dog.name = 'wangcai'
wangcai.shout()
print(wangcai.name)
print(Dog.name)


# Multiple Inheritance
class Mix(Cat, Dog):
	def __init__(self, name):
		# super.__init__(Cat, self, name)
		# super.__init__(Dog, self)
		pass

mix = Mix('mix')
mix.shout()
mix.power()
mix.favorite()


class Sample():
	def __private_func(self):
		print('private func')
	def public_func(self):
		self.__private_func()
		print('public func')
	def static_func():
		print('statuc func')

	@staticmethod
	def static_method():
		print('static method')

s = Sample()
# Error
# s.__private_func()
s._Sample__private_func()
s.public_func()
Sample.static_func()
Sample.static_method()

# Oparator Override
class People():
	def __init__(self, name, age):
		self.age = age
		self.name = name
	def __add__(self, other):
		return People(self.name, self.age + other.age)
	def __str__(self):
		return 'name: ' + self.name + ', age: ' + str(self.age)
	def test(self):
		print('test')

xiaoming = People('xiaoming', 24)
xiaoqiang = People('xiaoqiang', 25)
xiaoming += xiaoqiang
print(xiaoming) # name: xiaoming, age: 49

# Python introspection
print(id(People))
print(repr(xiaoming)) # <__main__.People object at 0x02858E10>
print(str(xiaoming)) # name: xiaoming, age: 49
print(type(xiaoming)) # <class '__main__.People'>
print(dir(xiaoming))
print(vars(xiaoming)) # {'name': 'xiaoming', 'age': 49}
print(hasattr(xiaoming, "age")) # True
setattr(xiaoming, "age", 50)
print(xiaoming) # name: xiaoming, age: 50
delattr(xiaoming, "age")
print(hasattr(xiaoming, "age")) # False
print(hasattr(xiaoming, "test")) # True
print(callable(xiaoming.name)) # False
print(callable(xiaoming.test)) # True
print(issubclass(People, Animal)) # False
print(issubclass(Mix, Animal)) # True
print(isinstance(xiaoming, People)) # True
print(isinstance(xiaoming, Animal)) # False