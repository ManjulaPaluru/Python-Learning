# Approach 1
#Module is a collection of functions, python file is called module
# Bt importing module to another module we can acces the other module functions.
import calculator
calculator.add(1,2)
calculator.mul(1,2)

# Approach 2
from calculator import add,mul
add(1,2)
mul(1,2)
# Approach 3
from calculator import *
add(1,2)
mul(1,2)