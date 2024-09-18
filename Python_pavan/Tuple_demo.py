mytuple =("a","b","c")
print(mytuple)
print(mytuple[0]) #a
# reding tuple items using for loop
for i in mytuple:
    print(i)
print(max(mytuple))
print(min(mytuple))
print(mytuple[1:2])
if "a" in mytuple:
    print("a is in tuple")
else:
    print("a is not in tuple")
# we can't modify the tuple, means add, remove, appemd, extend.
# we have one way to do or that need to convert tuple to list ,
# do modifications and covert back to tuple
mytuple1 =(1,2,3,4)
print(mytuple1)
mylist1 =list(mytuple1)
print(mylist1)
mylist1.append("a")
print(mylist1)
mytuple1 = tuple(mylist1)
print(mytuple1)
# copy one tuple to another tuple is positible wihtout changing data
mytuple3 = mytuple
print(mytuple3)
# joining and concatination is posible with tuples
mytuple4 =mytuple3+mytuple1
print(mytuple4)
if mytuple4 == mytuple3:
    print("mytuple4 and mytuple3 both are equal")
else:
    print("mytuple4 and mytuple3 both are not equal")