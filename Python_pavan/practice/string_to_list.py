#1.  convert string to list
import collections
from shlex import join

string1 = "manjula"
print(list(string1))

# 2. convert list to string by using join method
list1 = ['s','t','o','p', '1']
list2  =''.join(list1)
print(list2)
list3 =join(list1)
print(list3)
list4 ='123'.join(list1)
print(list4)

# 3 what does zip() will do in python , it will take input from multiple iterables and give single iterable of tuple
l1 = [1,2,3]
l2 = [9,8,7]
l3 = zip(l1,l2)
print(list(l3))

l1 = [1,2,3]
l2 = [9,8,7]
l3 = [0,0,0]
l4=zip(l1,l2,l3)
print(list(l4))

#8 when are dictonary,list,set used?
# If we want to maintain insertion order go for list
# if we don't want to maintain insertion order go for set
# if you want to store values into key and value pair go for dictonary, it won't follow the insertion order
# If we want to preserve the insertion order for dictonary we need to import the collections class and use the method orderedDict() method

dict1 ={1:'a',2:'b',3:'c'}
print(dict1)
print(collections.OrderedDict(dict1))