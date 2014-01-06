#-*- encoding: utf-8 -*-

# Date Types
print(type(1)) # <class 'int'>

print(type(1.1)) # <class 'float'>

print(type(0xff)) # <class 'int'>

print(type(0o34)) # <class 'int'>

print(type("hello world")) # <class 'str'>

print(type(True)) # <class 'bool'>

print(type(b'hello world')) # <class 'bytes'>

print(type(None)) # <class 'NoneType'>

print(type([])) # <class 'list'>

print(type(())) # <class 'tuple'>

print(type({})) # <class 'dict'>

print(type(set())) # <class 'set'>

# Help Methods
print(dir(str))

print(dir("abc"))

#print(help(str))

# int and float
var = 65
if isinstance(var, int):
	print("var is a int")
print(ord("A")) # 65
print(ord("a")) # 97
print(chr(var)) # A
print(int("29")) # 29
# Error
#print(int("2.4"))
print(float("2.9")) # 2.9
print(int(2.9)) # 2
print(float(29)) # 29.0
print(int("FF", 16)) # 255
print(int("29", 16)) # 41
print(oct(29)) # 0o35
print(hex(29)) # 0x1d
#+-*/
print(11//2) # 5
print(-11//2) # -6
print(11.0//2) # 5.0
print(2**8) # 256
a = 1
a += 1
print(a) # 2
# Error
# a++

# str
print(len("hello world")) # 11

print("Hello world".startswith("he")) # False

print("Hello world".upper().startswith("HE")) # True

print("Hello world"[1:10]) # ello worl

print("Hello world"[1:-1]) # ello worl

print("Hello world"[:-1]) # Hello worl

print("Hello world"[1:]) # ello world

for c in "hello world":
	print(c)

name = 'Riley'
age = 24
print("Hello %s" % name) # Hello Riley
print("Hello {0}".format(name)) # Hello Riley
print("Hello %s,Age %d" % (name, age)) # Hello Riley,Age 24

# Error
#print('The number is ' + 3)
print('The number is ' + str(3))
print('The number is ' + repr(3))

multiple_line_str = """
 a multiple
 line
 str
"""
print(multiple_line_str)

print("*"*10) # **********

# bytes
print('hello world'.encode('utf-8')) # b'hello world'

# None
print(not not None) # False
print(None == None) # True
print(None is None) # True

a = None

# Error
#if w is None:
#	print('w is None')

if a is None:
	print('a is None')

if a == None:
	print('a is None')


# list
l = ['a', 'simple', 'list', 'with', 'six', 'elements']

print(l[0]) # a
print(l[1]) # simple
print(l[-1]) # list
print(l[:3]) # ['a', 'simple', 'list']
print(l[3:]) # ['with', 'six', 'elements']
print(l[3:4]) # ['with']

l += [2.0, 3]
# or l = l + [2.0, 3]
print(l) # ['a', 'simple', 'list', 'with', 'six', 'elements', 2.0, 3]
l.append(True)
print(l) # ['a', 'simple', 'list', 'with', 'six', 'elements', 2.0, 3, True]
l.extend(['hello', 'hello'])
print(l) # ['a', 'simple', 'list', 'with', 'six', 'elements', 2.0, 3, True, 'hello', 'hello']
l.insert(0, 'zero')
print(l) # ['zero', 'a', 'simple', 'list', 'with', 'six', 'elements', 2.0, 3, True, 'hello', 'hello']

print(l.count('hello')) # 2
print(l.index(2.0)) # 7
print(3 in l) # True

del l[0]
print(l) # ['a', 'simple', 'list', 'with', 'six', 'elements', 2.0, 3, True, 'hello', 'hello']
l.remove('hello')
print(l) # ['a', 'simple', 'list', 'with', 'six', 'elements', 2.0, 3, True, 'hello']
print(l.pop()) # hello
print(l) # ['a', 'simple', 'list', 'with', 'six', 'elements', 2.0, 3, True]

# dir(l)
print(not not []) # False
print(not not l) # True

# tuple
t = ('a', 'simple', 'tuple', 'with', 'six', 'elements')

print(t[0]) # a
print(t[:3]) # ('a', 'simple', 'tuple')
print(t[3:]) # ('with', 'six', 'elements')

print('six' in t) # True
print('seven' in t) # False

print(t.index('with')) # 3
print(t.count('with')) # 1

print(tuple(l)) # ('a', 'simple', 'list', 'with', 'six', 'elements', 2.0, 3, True)
print(list(t)) # ['a', 'simple', 'tuple', 'with', 'six', 'elements']

v = ('a', 2, True)
x, y, z = v
print(x) # a
print(y) # 2
print(z) # True

a, b = 2, 3
print(a) # 2
print(b) # 3

def multi_return_value(num1, num2):
	return num1 + num2, num1 - num2

add, sub = multi_return_value(4, 3)
print(add) # 7
print(sub) # 1

params = (5, 2)
add, sub = multi_return_value(*params)
print(add) # 7
print(sub) # 3

print(type((False))) # <class 'bool'>
print(type((False,))) # <class 'tuple'>

# set
s = {1, 2, 3, 4, 5, 6}
print(s) # {1, 2, 3, 4, 5, 6}
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6}
print(s1.intersection(s2)) # {3, 4}
print(s1.difference(s2)) # {1, 2}
print(s2.difference(s1)) # {5, 6}
l = [1, 2, 3, 4, 5, 6, 5, 4]
print(set(l)) # {1, 2, 3, 4, 5, 6}

s = set()
s.add(1)
s.add(3)
s.add(3)
print(s) # {1, 3}
print(len(s)) # 2
s.update({3, 6, 9}, {1, 2, 3, 5, 8, 13})
print(s) # {1, 2, 3, 5, 6, 8, 9, 13}
s.update([10, 20, 30])
print(s) # {1, 2, 3, 5, 6, 8, 9, 10, 13, 20, 30}

s.remove(1)
print(s) # {2, 3, 5, 6, 8, 9, 10, 13, 20, 30}
s.discard(2)
print(s) # {3, 5, 6, 8, 9, 10, 13, 20, 30}
#KeyError: 1
#s.remove(1)
s.discard(2)
print(s.pop()) # 3
print(s) # {5, 6, 8, 9, 10, 13, 20, 30}
s.clear()
print(s) # set()

print(not not s) # False

# dict

d = {"a": 1, "b": 2, "c": 3}
print(d) # {'a': 1, 'c': 3, 'b': 2}
d["a"] = 0
print(d) # {'a': 0, 'b': 2, 'c': 3}
d["d"] = 4
print(d) # {'d': 4, 'b': 2, 'c': 3, 'a': 0}
print("d" in d) # True
print(len(d)) # 4
print(not not {}) # False

# bool
print(0 == False) # True
print(1 == True) # True
print(2 == True) # False