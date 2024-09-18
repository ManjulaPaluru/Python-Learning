# declaring list, list is ordered based on stores different collection of items.
'''mylist1 = ["apple",10,"watermelon"]
mylist2 = ["apple","orange"]
mylist3 = [10,20,30]
mylist = list()
print(mylist2)
print(mylist)
# How to access items from the list
mylist4 =["apple",10,"watermelon"]
print(mylist4[1]) #10
# print(mylist4[-1]) #watermelon'''
# Range of indexes
# mylist =["apple","orange","banana","grapes","watermelon","mango"]
# # count or total number of the items in a list
# print("total no of items: {}".format(len(mylist)))
# # reading the list items using loop
# for i in mylist:
#     print(i)
# print("*************")
# # check if the item is exit in the list or not
# if "grapes" in mylist:
#     print("grapes in the list")
# else:
#     print("grapes in not in the list")
# print(mylist[3:5]) #['grapes', 'watermelon']
# print(mylist[-5:-1]) #['orange', 'banana', 'grapes', 'watermelon']
# # how to change the item value from the list
# mylist[0]="guva"
# print(mylist)
# # Add new item to the list, we have 2 methods append(), insert()
# mylist.append("jira") # adding new item in to end of the list
# print(mylist)
# mylist.insert(1,"avocado") # It will insert any place in list based on given index
# # insert function we need to give 2 parameters like position and value.
# # It will insert any place in list based on given index
# print(mylist)
# # Remove the item from the list . using pop(),clear(), 'del' is a keyword, no need to use brackets
# print(mylist) # ['guva', 'avocado', 'orange', 'banana', 'grapes', 'watermelon', 'mango', 'jira']
# mylist.pop(0) # item will be removed based on index position
# print(mylist) #['avocado', 'orange', 'banana', 'grapes', 'watermelon', 'mango', 'jira']
# del mylist[2]
# print(mylist) #['avocado', 'orange', 'grapes', 'watermelon', 'mango', 'jira']
# mylist.clear() # clear all the items from the list
# print(mylist) # [] clear function will remove all items from the list
# #copy list list(),copy()
# mylist1 = ["a","b","c"]
# mylist2 =list(mylist1) # using list function to copy one list to another
# print(mylist2)
# mylist3 =mylist1.copy()
# print(mylist3)
# #Example 11 combine and joins lists , by using  +, for loop with append() and extend()
# l1=["a","b","c"]
# # l2=[1,2]
# # l3 =l1+l2
# # print(l3) #['a', 'b', 'c', 1, 2]

# using loop for concating or joining 2 lists
l1=["a","b","c"]
l2=[1,2]
for i in l1:
    l2.append(i)
print(l2)

# using extend()
l1=["a","b","c"]
l2=[1,2]
l2.extend(l1)
print(l2)

l1=["a","b","c"]
l2=[1,2]
l2.append(l1)
print(l2)
l3=l2.copy()

l1.append("d")
print(l2)
l2[2].remove("c")
print(l2)
print(l1)

print(l3)

