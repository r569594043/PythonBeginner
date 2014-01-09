#-*- encoding: utf-8 -*-
'''
	Python Standard Library
	See Also: http://docs.python.org/3/library/index.html
'''

import re
'''
	re
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
print(time.strptime('2014-01-09 17:33:30', '%Y-%m-%d %H:%M:%S')) # time.struct_time(tm_year=2014, tm_mon=1, tm_mday=9, tm_hour=17, tm_min=33, tm_sec=30, tm_wday=3, tm_yday=9, tm_isdst=-1)

print(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')) # 2014-01-09 17:45:25

t = time.strptime('2014-01-09 17:33:30', '%Y-%m-%d %H:%M:%S')

print(time.strftime('%m/%d/%y %I:%M:%S %p', t)) # 01/09/14 05:33:30 PM