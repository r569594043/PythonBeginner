#-*- encoding: utf-8 -*-

class Animal():
	"""Animal Class"""

	name = "Animal"

	def __init__(self):
		self.className = 'Animal'

class Cat(Animal):
	"""Cat Class"""
	name = 'Cat'

	def __init__(self, name):
		super(Animal, self).__init__()
		self.className = 'Cat'
		self.name = name
	def shout(self):
		print(self.name + ' shout: miao~')
	def favorite():
		print('my favorite food is fish')


class Dog(Animal):
	"""Dog Class"""
	def __init__(self):
		super(Animal, self).__init__()
		self.className = 'Dog'
	def shout(self):
		print(self.name + ' shout: wang~')
	def power():
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




# Mix
class Mix(Cat, Dog):
	def __init__(self, name):
		super.__init__(Cat, self, name)
		super.__init__(Dog, self)

mix = Mix('mix')
mix.shout()
mix.power()
mix.favorite()