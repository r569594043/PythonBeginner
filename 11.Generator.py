def where(l, func):
	for e in l:
		if func(e):
			yield e

def select(l, func):
	for e in l:
		yield func(e)

for i in where([6, 7, 4, 2, 9, 8, 1], lambda e: e % 2 == 0):
	print(i)

print(type(where([6, 7, 4, 2, 9, 8, 1], lambda e: e % 2 == 0))) # <class 'generator'>

for i in select([6, 7, 4, 2, 9, 8, 1], lambda e: e * 2):
	print(i)

def odd():
	i = 0
	while True:
		yield i * 2 + 1
		i += 1

def even():
	i = 0
	while True:
		yield i * 2
		i += 1

# for i in odd():
#	print(i)

class Fib:
    '''生成菲波拉稀数列的迭代器'''

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

for i in Fib(100):
	print(i)