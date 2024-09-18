# class myclass:
#     @staticmethod
#     def mymethod1(self):
#         print("instance method")
#     def mymethod2(self):
#         print("static method")
# myclass.mymethod1(1)  # static method we can acces through classname, but we need to pass value to self parameter  while calling the method, bec here self teat as a parameter.
#
# mc2 = myclass() # through object we can access instance methods , no need to pass the parameter for self keyword, if this is instance method
# mc2.mymethod2()

# Global, class ,local varables accing in class

g1, g2 =10,20 # Global variables
class myclass:
    c1 ,c2 = 1,2 # class level variables
    def add(self,l1,l2):
        print( "local variables: {}".format(l1+l2))    # accessing local variables
        print("class level variables {}".format(myclass.c1+self.c2)) # class level variables we can access through class name or self keyword
        print("global variables {}".format(g1 + g2)) # global variables we can access from anywhere
mc = myclass()
mc.add(5,6)
print("**********")
# example 3
g1 ,g2 =1,2
class myclass:
    g1,g2 = 3,4
    def add(self):
        g1,g2 =5,6
        print("Local variable {}".format(g1+g2))
        print("class levle variables {}".format(self.g1 + self.g2))
        print("global variables {}".format(globals()['g1']+ globals()['g2']))
mc = myclass()
mc.add()
print("********")

g1= 2
def add(self):
    global g1
    g1 = 9
    print(g1)
print(g1)
add(1)
# constructor example
class myclass:
    name = "manju"
    def __init__(self,name):
        print(name)
        print(self.name)
        print("this is constructor")
    def m1(self):
        print("method executing")
obj1 = myclass("suneel")
obj1.m1()
# Example emp: constructor  = eid, ename, esal
# display() , print  eid, ename, esal
print("&&&&&&&&&")
class myclass:
    def __init__(self,eid, ename, esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal
        print("default constructor")

    def display(self):
        print(self.eid)
        print(self.ename)
        print(self.esal)
obj1= myclass(1,"manju",5000)
obj1.display()


