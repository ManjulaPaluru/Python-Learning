# list is data type and it will store multiple values with different data types

values = [1, 2, 5, "manju", 10]
print(values[0])    # first one
print(values[3])    # 4 value
print(values[-1])    # last value from list
# values[#starting index:endingindex-1]
# [2, 5] will print her till 2 nd index value because in python last index 3 means it will give result as 3-1
print(values[1:3]) #
# inserting value in 3 rd position
values.insert(3, "paluru")
print(values)
# append will add the new value into the end of the list
values.append("saguturu")
print(values)
# updating the value in list
values[3] = "Medha" # paluru 3 index value is replaced with Medha
print(values)

ar = [111, 44, 3, 2]
print(ar)
print(values.__sizeof__())