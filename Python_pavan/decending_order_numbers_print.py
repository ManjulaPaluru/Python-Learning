# printing decending order no
i = 10
while(i>=1):
    print(i)
    i = i -1
print("***************")
for i in range(10):
    print(i)
print("***************")
for i in range(2,100,2):
    print(i)
print("***************")
for i in range(10,0,-1):
    print(i)
print("***************")
#exit the program while loop reach the 5 using break. here once if condition is true it will exit from the loop
for i in range(1,10):
    if i == 5 or i==2:
        break
    print("i values are : ",i)
print("condition satisfied, exit from loop")
print("***************")
#exit the program while loop reach the 5 using continue .
#if the if condition is true here 5 won't print. before 5 and after 5 numbers will print,
for i in range(1,10):
    if i == 5 or i==3 or i==2:
        continue
    print("i values are : ",i)
print("condition satisfied, exit from loop")
print("***************")
for i in range(3,7,2):
    print(i)


