# Global and Local variables
# which is defined outside of the function is called global variables
# which ever variables are defined with in the function is called local variables.
# We can access global variables outside and inside of the function.
# Local variable scope is with in the function only, will get complile error "unresolved reference local variable
# GLOBAL VARIABLES WE CAN CREATE INSIDE FUNCTION , BUT WE NEED TO REFER WITH 'global' KEYWORD'
# if we have both global and local  variables have same names,
# but if you  want access globle varible inside the method and want to change the value for futhere purpose
# we need to add variable name beside and  'global'  keyword. later that global variable value is changed values
# Example: 1

globle_var =20

def myfun():
    local_variable =10
    print("globle variable: ", globle_var)
    print("local_variable", local_variable)
myfun()
print("globle variable: ", globle_var)
print("***************")
#Example 2: global and local variable
x=100
def myfun():
    global x
    x = 200
    print("local variable:" ,x)

    print("globle variable: " ,x)
myfun()
print("now it is global variable,because of specified with 'global' keyword ", x)