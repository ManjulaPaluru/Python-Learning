
# Dictonary is collection of unordered, indexed and  mutable items. starts with {}, key and value pair.
mydict = {1:"a",2:"b",3:"c"}
print(mydict)
1. # accessing values from dictionary byusing key and get() also
print(mydict[1])
print(mydict[2])
mydict2 = {
    "brand": "Honda",
    "Model": "Rav4",
    "Model1": "Rav44",
    "Model2": "Rav444"
}
for i in mydict2:
    print(i) # print only keys from dictionary
    print(mydict2[i]) # print only values
for i in mydict2.values():
    print(i) # print  only values
for x, y in mydict2.items():
    print(x,y) # print keys along with value

print(mydict2)
print(mydict2["brand"])
print(mydict2.get("brand"))
# change the values from dictonary
mydict2["Model"] = "sv"
print(mydict2)
# how to check whether key is existing in dictonary
if "Model" in mydict2:
    print("exist")
else:
    print("not exist")
print("Model" in mydict2) # true single staement execution
# find number of  items in dictonary
print(len(mydict2))
# Add items to dectornary
mydict2["color"] = "Red"
print(mydict2)

# remove item from the dictonary y using pop(),del keyword
print(mydict2.pop("color"))
print(mydict2)
del mydict2["Model"]
print(mydict2)
# del mydict2 delete the hole dectionary
print(mydict2.clear())  # None will display
# #Xample 9 copy one dictionary to another dictionary, using copy() and without using copy()
mydict3 = mydict
print(mydict3)

mydict4= mydict.copy()
print(mydict4)