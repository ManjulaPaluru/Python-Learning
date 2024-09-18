# function
# function is a set of taks, start with def keyword.

def myfun():
    print("my function")
myfun()

# Example 2: passing parameters through function
def myfun(name):
    print("name is: " ,name)
myfun("manjula")
# Example 3: Function is returning the value
def myfun(a,b):
   return a+b;

result = myfun(2,3)
print(result)

print("results of a,b: ", myfun(10,20))
# Eaample 4: Returning none if we dont return vany value from function but menctined return keyword.
def myfun():
    return
print("returning none" ,myfun()) #None

def myfun():
    i =10
print(myfun()) #None
# Example 5:
def myfun(a,b):
    print(a+b)
print(myfun(1,2))




