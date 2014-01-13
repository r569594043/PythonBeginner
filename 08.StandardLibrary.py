#-*- coding: utf-8 -*-
'''
	Python Standard Library
	See Also: http://docs.python.org/3/library/index.html
'''

import re
'''
	Regular expression operations
	See Also: http://docs.python.org/3/library/re.html
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


import time
import datetime
'''
	strftime() and strptime() Behavior
	See Also: http://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
'''

print(time.strptime('2014-01-09 17:33:30', '%Y-%m-%d %H:%M:%S')) # time.struct_time(tm_year=2014, tm_mon=1, tm_mday=9, tm_hour=17, tm_min=33, tm_sec=30, tm_wday=3, tm_yday=9, tm_isdst=-1)

print(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')) # 2014-01-09 17:45:25

t = time.strptime('2014-01-09 17:33:30', '%Y-%m-%d %H:%M:%S')

print(time.strftime('%m/%d/%y %I:%M:%S %p', t)) # 01/09/14 05:33:30 PM

import math
'''
	Mathematical functions
	See Also: http://docs.python.org/3/library/math.html
'''

print(math.floor(5.5)) # 5
print(math.ceil(5.4)) # 6

print(math.pow(2, 4)) # 16.0

print(math.sqrt(16)) # 4.0

print(math.pi) # 3.141592653589793


import random
'''
	Generate pseudo-random numbers
	See Also: http://docs.python.org/3/library/random.html
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
	Higher-order functions
'''

l = [1, 2, 3, 4, 5]

def map_func(e):
	return e * 3

print([i for i in map(map_func, l)]) # [3, 6, 9, 12, 15]

print([i for i in map(lambda e: e * 4, l)]) # [4, 8, 12, 16, 20]


import functools
'''
	Higher-order functions and operations on callable objects
	See Also: http://docs.python.org/3/library/functools.html
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
'''
	Miscellaneous operating system interfaces
	See Also: http://docs.python.org/3/library/os.html
'''

print(os.getcwd()) # C:\Users\***\Desktop\PythonBeginner

os.chdir('c:/Windows')
print(os.getcwd()) # c:\Windows

print(os.getpid())

p = os.popen('ping /n 1 127.0.0.1')
print(p.read())
print(os.sep) # \
print(os.linesep) # \r\n
print(os.getenv('JAVA_HOME')) # C:\Program Files\Java\jdk1.6.0_43
print(os.name) # windows - nt / linux[unix] - posix
print(os.listdir('c:/'))
print(os.lstat('c:/test.txt'))
os.makedirs('c:/test/1/2/3/4/5')
os.mkdir('c:/test/1/2/3/4/5/6')
# Error
# os.mkdir('c:/test/1/2/3/4/5/6/7/8')
os.rmdir('c:/test/1/2/3/4/5/6')
# Error
# os.rmdir('c:/test')
# Error
# os.removedirs('c:/test')
os.removedirs('c:/test/1/2/3/4/5')
os.rename('c:/test.txt', 'c:/hello.txt')
# Error
# os.rename('c:/hello.txt', 'c:/1/hello.txt')
os.mkdir('c:/1')
os.rename('c:/hello.txt', 'c:/1/hello.txt')
os.renames('c:/1/hello.txt', 'c:/2/test.txt')
os.remove('c:/2/test.txt')
os.removedirs('c:/2')

'''
for basedir, dirs, files in os.walk('c:/'):
	for d in dirs:
		print(basedir + os.sep + d)
	for f in files:
		print(basedir + os.sep + f)
'''

import os.path
'''
	Common pathname manipulations
	See Also: http://docs.python.org/3/library/os.path.html
'''

print(os.path.basename('c:/test/1/2/3/4/5/6/7/8/test.txt')) # test.txt
print(os.path.dirname('c:/test/1/2/3/4/5/6/7/8/test.txt')) # c:/test/1/2/3/4/5/6/7/8
print(os.path.exists('c:/test/1/2/3/4/5/6/7/8/test.txt')) # False
os.makedirs('c:/test/1/2/3/4/5/6/7/8/')
print(os.path.exists('c:/test/1/2/3/4/5/6/7/8/')) # True
print(os.path.extsep) # .
# Return the last access time of a file
print(os.path.getatime('c:/windows/system32/cmd.exe')) # 1290309843.3325152
# Return the metadata change time of a file
print(os.path.getctime('c:/windows/system32/cmd.exe')) # 1290309843.3325152
# Return the last modification time of a file
print(os.path.getmtime('c:/windows/system32/cmd.exe')) # 1290309843.3325152
print(os.path.getsize('c:/windows/system32/cmd.exe')) # 302592
print(os.path.isdir('c:/test/1/2/3/4/5/6/7/8/')) # True
print(os.path.isfile('c:/test/1/2/3/4/5/6/7/8/')) # False
os.removedirs('c:/test/1/2/3/4/5/6/7/8/')
print(os.path.pardir) # ..
print(os.path.curdir) # .
print(os.path.pathsep) # ;
print(os.path.abspath('text.txt')) # c:\Windows\text.txt
print(os.path.relpath(r'c:\Windows\text.txt')) # text.txt
# Test whether two pathnames reference the same actual file
# print(os.path.samefile('c:/1.txt', 'c:/2.txt'))
print(os.path.sep) # \
print(os.path.split('c:/test/1/2/3/4/5/6/7/8/test.txt')) # ('c:/test/1/2/3/4/5/6/7/8', 'test.txt')
print(os.path.splitdrive('c:/test/1/2/3/4/5/6/7/8/test.txt')) # ('c:', '/test/1/2/3/4/5/6/7/8/test.txt')
print(os.path.splitext('c:/test/1/2/3/4/5/6/7/8/test.txt')) # ('c:/test/1/2/3/4/5/6/7/8/test', '.txt')
# print(os.path.stat.filemode(755)) # --wxrw--wt
print(os.path.join('c:/windows', 'cmd.exe')) # c:/windows\cmd.exe
print(os.path.join(r'c:\windows', 'system32', 'cmd.exe')) # c:\windows\system32\cmd.exe
print(os.path.join('c:/windows/', 'cmd.exe')) # c:/windows/cmd.exe

import sys

print(sys.argv) # ['C:\\Users\\RileyRen\\Desktop\\PythonBeginner\\08.StandardLibrary.py']
sys.stdout.write('Hello World') # Hello World
sys.stdout.flush()
# sys.stdin
# sys.stderr

import shutil
# abspath
# chown
# copy
# copy2
# copyfile
# copytree
print(shutil.disk_usage('c:/')) # usage(total=106690072576, used=69967917056, free=36722155520)
# move
# rmtree

import json

d = json.loads('{"name": "rxb", "age": 26}')
print(d) # {'name': 'rxb', 'age': 26}
print(d['age']) # 26
print(json.dumps(d)) # {"age": 26, "name": "rxb"}
# Serialize ``obj`` as a JSON formatted stream to ``fp``
# json.dump
# Deserialize ``fp``
# json.load

import hashlib

m = hashlib.md5()
m.update('hello world'.encode('utf-8'))
print(m.hexdigest()) # 5eb63bbbe01eeed093cb22bb8f5acdc3
m.update(open('c:/windows/system32/cmd.exe', 'rb').read())
print(m.hexdigest()) # 3b37a087052ba07ede4d74a638c92b85

import base64
a = base64.b64encode('Hello World'.encode('utf-8'))
print(a.decode())
print(base64.b64decode(a).decode())

import uuid
# uuid1: Generate a UUID from a host ID, sequence number, and the current time.
# uuid3: Generate a UUID from the MD5 hash of a namespace UUID and a name.
# uuid4: Generate a random UUID.
# uuid5: Generate a UUID from the SHA-1 hash of a namespace UUID and a name.
print(uuid.uuid1())
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'test'))
print(uuid.uuid4())
print(uuid.uuid5(uuid.NAMESPACE_DNS, 'testme'))


import pickle
# Write a pickled representation of obj to the open file object file.
# dump
# Read a pickled object representation from the open file object file and
# return the reconstituted object hierarchy specified therein.
# load
l = ['a', 'b', 'c', 'd']
p = pickle.dumps(l)
print(p) # b'\x80\x03]q\x00(X\x01\x00\x00\x00aq\x01X\x01\x00\x00\x00bq\x02X\x01\x00\x00\x00cq\x03X\x01\x00\x00\x00dq\x04e.'
print(pickle.loads(p)) # ['a', 'b', 'c', 'd']




