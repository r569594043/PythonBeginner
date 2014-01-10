#-*- encoding: utf-8 -*-
'''
	Python Standard Library
	See Also: http://docs.python.org/3/library/index.html
'''

import re
'''
	Regular expression operations
	See Also: http://docs.python.org/3/library/re.html
'''
'''
m = re.search('H(.*?)o', 'I Say: Hello World Hello World Hello World')

if m:
	print(m.group(0)) # Hello
	print(m.group(1)) # ell
	# Error
	# print(m.group(2))
else:
	print('no match')


m = re.match('H(.*?)o', 'I Say: Hello World Hello World Hello World')

if m:
	print(m.group(0))
	print(m.group(1))
else:
	print('no match') # no match

m = re.match('H(.*?)o', 'Hello World Hello World Hello World')

if m:
	print(m.group(0)) # Hello
	print(m.group(1)) # ell
else:
	print('no match')


# re.I or re.IGNORECASE

m = re.search('h(.*?)o', 'I Say: Hello World Hello World Hello World')

if m:
	print(m.group(0))
	print(m.group(1))
else:
	print('no match') # no match

m = re.search('h(.*?)o', 'I Say: Hello World Hello World Hello World', re.I)

if m:
	print(m.group(0)) # Hello
	print(m.group(1)) # ell
else:
	print('no match')

# re.M or re.MULTILINE

str = """
I Say:
Hello world,
Hello world,
Hello world,
"""
m = re.search('^h(.*?)o', str, flags = re.M | re.I)

if m:
	print(m.group(0)) # Hello
	print(m.group(1)) # ell
else:
	print('no match')

m = re.search('^H(.*?)o', str, re.I)

if m:
	print(m.group(0))
	print(m.group(1))
else:
	print('no match') # no match

print(re.sub('h(.*?)o', 'hey', 'I Say: Hello World Hello World Hello World', 2, re.I)) # I Say: hey World hey World Hello World

print(re.split('h.*?o', 'I Say: Hello World Hello World Hello World', 2, re.I)) # ['I Say: ', ' World ', ' World Hello World']

l = re.findall('h.*?o', 'I Say: Hello World Hello World Hello World', re.I)

for m in l:
	print(m)
	# Hello
	# Hello
	# Hello

re_hello = re.compile('h.*?o', re.I)

l = re_hello.findall('I Say: Hello World Hello World Hello World')

for m in l:
	print(m)
	# Hello
	# Hello
	# Hello

str = 'my str is this.\n'
# regex: this\.\n
m = re.search('this\\.\\n', str)

if m:
	print(m.group(0)) # this.\n
else:
	print('no match')

print('\n') # line break
print(r'\n') # \n

m = re.search(r'this\.\n', str)

if m:
	print(m.group(0)) # this.\n
else:
	print('no match')

# re.X or re.VERBOSE

m = re.search(r"""
	this # match this
	\.   # match .
	\n   # match break line
	""", str, re.X)

if m:
	print(m.group(0)) # this.\n
else:
	print('no match')

'''

import time
import datetime
'''
	strftime() and strptime() Behavior
	See Also: http://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
'''

'''
print(time.strptime('2014-01-09 17:33:30', '%Y-%m-%d %H:%M:%S')) # time.struct_time(tm_year=2014, tm_mon=1, tm_mday=9, tm_hour=17, tm_min=33, tm_sec=30, tm_wday=3, tm_yday=9, tm_isdst=-1)

print(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')) # 2014-01-09 17:45:25

t = time.strptime('2014-01-09 17:33:30', '%Y-%m-%d %H:%M:%S')

print(time.strftime('%m/%d/%y %I:%M:%S %p', t)) # 01/09/14 05:33:30 PM
'''

import math
'''
	Mathematical functions
	See Also: http://docs.python.org/3/library/math.html
'''
'''
print(math.floor(5.5)) # 5
print(math.ceil(5.4)) # 6

print(math.pow(2, 4)) # 16.0

print(math.sqrt(16)) # 4.0

print(math.pi) # 3.141592653589793
'''

import random
'''
	Generate pseudo-random numbers
	See Also: http://docs.python.org/3/library/random.html
'''
'''
print(random.random())
print(random.randint(0, 99))
print(random.randrange(0, 100, 5))
print(random.uniform(10.5, 21.3))
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8]))
l = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(l)
print(l)
print(random.sample(l, 3))
'''


'''
	Higher-order functions
'''
'''
l = [1, 2, 3, 4, 5]

def map_func(e):
	return e * 3

print([i for i in map(map_func, l)]) # [3, 6, 9, 12, 15]

print([i for i in map(lambda e: e * 4, l)]) # [4, 8, 12, 16, 20]
'''

import functools
'''
	Higher-order functions and operations on callable objects
	See Also: http://docs.python.org/3/library/functools.html
'''
'''
users = [{
	'name': 'xiaoming',
	'age': 50
}, {
	'name': 'xiaoqiang',
	'age': 45
}, {
	'name': 'xiaoli',
	'age': 35
}]


def reduce_func(init, user):
	return init + user['age']

print(functools.reduce(reduce_func, users, 0)) # 130

print(functools.reduce(lambda i, u: i + u['age'], users, 0)) # 130

l = [1, 2, 3, 4, 5]
print(functools.reduce(lambda i, e : i + e, l)) # 15
'''

'''
	See Also: http://docs.python.org/3/library/functions.html#open
'''
f = open('c:/test.txt', 'w', encoding = 'utf-8')
f.write('Hello World!\n')
f.write('Hello World!\n')
f.write('Hello World!\n')
f.writelines(['Hello World, ', 'Hello World, ', 'Hello World!']);
f.flush()
print(f.writable()) # True
f.close()
print(f.closed) # True

f = open('c:/test.txt', 'r')
for l in f.readlines():
	print(l.strip())
f.close()

f = open('c:/test.txt', 'r')
for l in f:
	print(l.strip())
f.close()

f = open('c:/test.txt', 'rb')
print(f.read()) # b'Hello World!\r\nHello World!\r\nHello World!\r\nHello World, Hello World, Hello World!'
print(f.read()) # b''
f.seek(0)
print(f.read()) # b'Hello World!\r\nHello World!\r\nHello World!\r\nHello World, Hello World, Hello World!'
f.seek(10)
print(f.read()) # b'd!\r\nHello World!\r\nHello World!\r\nHello World, Hello World, Hello World!'
f.seek(0)
print(f.read().decode('utf-8').split('\r\n')) # ['Hello World!', 'Hello World!', 'Hello World!', 'Hello World, Hello World, Hello World!']
print(f.writable()) # False
f.close()

import os
print(os.getcwd()) # C:\Users\***\Desktop\PythonBeginner