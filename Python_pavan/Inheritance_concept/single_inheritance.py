#Example 1 single inheritance
class A:
    def m1(self):
        print("parent class")
class B(A):
    def m2(self):
        print("child class")
bobj = B()
bobj.m1()
bobj.m2()

#Eample 2

class A:
    x,y =10,20
    def m1(self):
        print(self.x + self.y)
class B(A):
    a,b = 3,4
    def m2(self):
        print(self.a + self.b)
        print(self.x + self.y)
obj = B()
obj.m1()
obj.m2()

class A:
    name ="manju"
class B(A):

    name = "anju"

    def test(self):
        print(super().name)

bobj = B()
print(bobj.name)
bobj.test()


