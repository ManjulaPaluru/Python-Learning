# 2 types of parameters/arguments
#positional parameters  and keyword parameters
# we can pass positional and keyword arguments combined. But one rule is there,
# positional arguments always need to write before keyword parameters

def myfun(x,y):
    print(x,y)
myfun(1,2) # positional arguments:
myfun(x=20,y=30)
# keyword parameters
# default values assigned to positional agruments
def myfun(x, y=1):
    print(x,y)
myfun(10,20)
myfun(0)

#
def myfun(name, greetingmessage):
    print(greetingmessage+" "+ name)
myfun("manju", "hello")
myfun(greetingmessage= "HELLO",name="MANJU")

#
def myfun(a,b,c):
    print(a,b,c)
myfun(10,20,30)
myfun(a = 10,b =20,c=30)
#myfun((a=10,20,30))  # syntax error, bec positional parameter need to first always
#myfun(10,30,b=20) # there is no syntax error ,but logical error TypeError: myfun() got multiple values for argument 'b'

#Function can return multiple values
def largest(a,b):
    if a>b:
        return a,b
    else:
        print("b is largest value")
        return b,a
res = largest(20,30)
print(type(res))
print(largest(30,20))