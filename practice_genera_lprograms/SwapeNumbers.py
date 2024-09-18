#swapping two numbers whtout using temp

x=4
y=5
x,y = y,x
print("x", +x)
print("y" ,+y)
# swapping two numbers using temp variable
a=10
b=20
temp=a
a=b
b=temp
print("a value after swaping:{}". format(a))
print("b value after swapping:{}". format(b))
# entering input in runtime
c = input("enter c value: ")
d = input("enter d value: ")
c, d =d, c
print("c,d vlues after swapping :{} {} " .format(c,d))