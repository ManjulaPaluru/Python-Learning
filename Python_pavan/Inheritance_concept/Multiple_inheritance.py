class parent1:
    def m1(self):
        print("parent one")
class parent2:
    def m2(self):
        print("parent two")
class child(parent1,parent2):
    def m3(self):
        print("child class")
child_obj =  child()
child_obj.m3()
child_obj.m2()
child_obj.m1()



class A:
    def m1(self):
        print("parent class m1 method")
class B(A):
    def m1(self):
        super().m1()
        print("child class m1 method")
bobj = B()
bobj.m1()
