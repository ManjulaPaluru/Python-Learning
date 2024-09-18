# Approach 1 by using direct importing the module
import Class1 # these are module name
import Class2
class OneTwo:
   obj_one =Class1.One() # creating object for class one by using module name dot
   obj_one.display()
   obj_two =Class2.Two() # creating object for class Two by using module name dot
   obj_two.display()

# Approach 2:
from Class1 import One
from Class2 import Two
obj = One()
obj.display()
obj1 = Two()
obj.display()