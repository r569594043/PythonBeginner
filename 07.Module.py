#-*- coding: utf-8 -*-
'''
	Modules
	See Also: http://docs.python.org/3/tutorial/modules.html
'''

import ModuleA
from ModuleB import func
from ModuleB import func1 as b_func1
import ModuleB
import ModuleC
# import ModuleC.Class2

ModuleA.func() # func in ModuleA
ModuleA.func1() # func1 in ModuleA
func() # func in ModuleB
b_func1() # func1 in ModuleB

c = ModuleB.Class2()
print(c) # <ModuleB.Class2 object at 0x027A5F50>
c = ModuleC.Class3()
print(c) # <ModuleC.Class3 object at 0x027A5F10>
# Error
# c = ModuleC.Class4.Class4()

from ModuleC import *
c = Class3() # <ModuleC.Class3 object at 0x028789F0>
print(c)
c = Class4.Class4() # <ModuleC.Class4.Class4 object at 0x02878A10>
print(c)
