import os
import sys
import django
print(django.VERSION)
sys.path.append('/home/sol/hill')
print(sys.path)
#from module import *
#from module2 import *
#from module import calc_total_price
from fmodule import module
#import module2

print(dir())
z = module.calc_total_price(price=123, discount=2, z=123)
print(z *8)
