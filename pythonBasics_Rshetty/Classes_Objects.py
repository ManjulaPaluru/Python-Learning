# Self keyword is mandatory for  calling variables name into methods
# class varibales are constant
# instance variables are different for every object
# when i create the object ,object will be passed as first argument to the constructor by defalt. by using that self we can create instance variables
# fno, secno are instance variables , for instance variables we need to use self.
# If we are using class variables in within the class we can access through self and class name,
# but outside the class means, need to access through object rference.


class Calculator:
    num = 100 # class variables
    # default constructor
    print(num)
    def getData(self):
        print(" I am  now executing as method in class ")
        print(self.num)

    def __init__(self, a, b):
        print("I am default constructor , i am calling while creating the object")
        #
        self.fno = a
        self.secno =b
    def summation(self):
       return self.fno + self.secno+self.num



obj = Calculator(2, 3)    # syntax to create object in python, no need to use new keyword
obj.getData()
print(obj.num)
print(obj.summation())

