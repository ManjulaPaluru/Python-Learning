class A:
    def m1(self):
        print("parent class A")
class B(A):
    def m2(self):
        print("child class B")
class C(A):
    def m3(self):
        print("child class C")

bobj = B()
bobj.m1()
bobj.m2()
cobj = C()
cobj.m1()
cobj.m3()