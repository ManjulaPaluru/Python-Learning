# write a program print sum  of distent elements
list = [1,5,3,6,8,1,3,5]
total =0
setlistt = set(list)
print(setlistt)
for i in setlistt:
    total = i+total
print(total)

print("************************")

list = [1,8,5,3,6,8,1,3,5,5]
total = 0
list1 = []
for i in list:
    if i in list1:
        continue
    else:
        list1.append(i)
        total = i + total

print(list1)
print(total)


total = 0
set1 = set()
for i in list:
    if i in set1:
        continue
    else:
        set1.add(i)
        total = i + total

print(list1)
print(total)
print("******************")

# st = set(i for i in list)
print(sum(set(i for i in list))) # single line statement
