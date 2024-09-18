# printing programetaclly version of the python using
import sys
print(sys.version)

# how do you find the no of objects refering to the particular object.
x="manjula"
y=x
print(sys.getrefcount(x))

#sorting list in numerical order
list = [200,4,63,7,1]
temp =0
for i in range(0,list.__len__() ,1):
    for j in range(i+1,list.__len__(),1):
        if(list[i] >list [j]):
            temp=list[i]
            list[i] = list[j]
            list[j]=temp
for k in range(0,list.__len__(),1):
    print(list[k])


list2 = [2,4,1,0,10]
for i in list2:
    list2.sort()
print(list2)


list3 =[30,1,2,0,200]
list3 = [int(i) for i in list3],list3.sort(),print(list3)

# If we are nt giving any brackets, python treats a tuple, its called tuple packing, output is (10,20,30)
A = 10,20,30
print(A)
print(type(A))

A = 2,3,4,5
a,b,c,d =A
print(a)
print(b)
print(c)
print(d)
# deleting variable in python
del(a)

# in python 3 does not support the octal number, giving syntax error for a=0101, in python 2 it will work treat like 65 +2
'''a = 0101
b=2
c=a+b
print(c)'''
# what is for - else and while - else in python: the loop is not satisfied the condition else we can use.
a=[10,20,30]
for i in a:
    print("in for loop")
else:
    print("in else loop")

a = range(1,100)
for i in a:
     print(i)
print(type(a))

# slicing
# syntax  list/tuple[startingindex:endindex:step]
a=[100,200,300,400,500,600,700,800]
print(a[2::3])


# append() and extend()
a = [1,2,3,4,5]
b= [6,7,8]
a.extend(a)
print(a)
a.append(b)
print(a)
c = ['a','b']
a.extend(c)
print(a)
a.append(c)
print(a)
# declaring variables in single line and printing in single line
name,age,sal ="manju",30,4000
print(name,age,sal)
print("Name is: ", name)
#approach 3 representing print statement in one stament
print("Name is: %s Age is: %d Sal is: %g" %(name,age,sal))
# using format method
print("name is: {} age is: {} sal is: {}".format(name,age,sal))
# type of variabe
num1 = input("enter no: ")
print(type(num1))
# we can also use if else condition in single line (ternary operator)
# print given no is even or odd
num=11
print("even no") if num%2==0 else print("odd no")
# if else multiple statements in single line printing
a=9
{print("hi"),print("hello")} if a>=10 else {print("java"),print("python")}

{print("one"),print("two"),print("three")} if a>5 else {print("hi"),print("bye")}

# print multiple conditions using elif
weekno = int(input("enter the weekno: "))
if weekno ==1:
    print("sunday")
elif weekno ==2:
    print("Monday")
elif weekno ==3:
    print("tuesday")
elif weekno ==4:
    print("wednesday")
elif weekno ==5:
    print("Thursday")
elif weekno==6:
    print("friday")
elif weekno ==7:
    print("Friday")
# positive or nagitive no
num = int(input("enter no for finding positive/nagative no: "))
print("positive no: %d " %(num)) if num > 0 else print("nagtive no")
# checking the largest of 3 no


def maximum(a,b,c):
    if a > b and a > c:
        print("a is greater")
    elif b > c:
        print("b is greater")
    else:
        print("c is greater")
    print("a") if a>b and a > c else print("b") if b > c else print("c")


maximum(4,2,3)
maximum(4,2,9)
maximum(4,9,3)






