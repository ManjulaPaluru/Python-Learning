# write ap program to convert below 2 lists to dictonary

list1 =["manju","anju","medha","he"]
list2 = [12345,345456,343454,78979]
dic ={}
for i in range(0, len(list1)):
    dic[list1[i]] = list2[i]
print(dic)

# Approach 2 : convert list to dictionary by using zip
def list_to_dict():
    list1 = [1,2,3,4]
    list2 = ["one","two","three"]
    result = dict(zip(list1,list2))
    print(result)

list_to_dict()

# convert dictionary to tuple
def dic_to_tuple():
    dic = {1: 'one', 2: 'two', 3: 'three'}
    for i in dic.items():
        print(i)
dic_to_tuple()
