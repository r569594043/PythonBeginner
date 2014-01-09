#-*- coding: utf-8 -*-
'''
	Control Flow
	See Also: http://docs.python.org/3/tutorial/controlflow.html
'''


var = 4

if var % 2 == 1:
	print("It's a odd number")
else:
	print("It's a even number")


var = "5"

if var.isnumeric() and int(var) % 2 == 1:
	print("It's a odd number")
elif var.isnumeric() and int(var) % 2 == 0:
	print("It's a even number")
else:
	print("It's not a number")

print(5 or False) # 5
print(0 and 1) # 0
print(5 or 7) # 5
print(5 and 7) # 7

print(not 0) # True


for i in range(10):
	print("hello world " + str(i))

l = [1, 2, 3, 4, 5]

for e in l:
	print(e)

for i in range(len(l)):
	print(l[i])

for i in range(0, 10, 2):
	print(i)

for i in range(0):
	print(i)
else:
	print("no data")

i = 0
while i < 10:
	print(i)
	if(i == 5):
		break
	i += 1

while False:
	print("data")
else:
	print("no data")


try:
	print(a)
except Exception as ex:
	print(ex)
finally:
	print('finally')

try:
	print(var)
except:
	print("error")
else:
	print("There is no error")


try:
	print(var)
except:
	print("error")
else:
	print("There is no error")

x = 3
print('even' if x % 2 == 0 else 'odd') # odd

# List Comprehensions
odds = [i for i in range(100) if i%2 == 0]

print(odds)

