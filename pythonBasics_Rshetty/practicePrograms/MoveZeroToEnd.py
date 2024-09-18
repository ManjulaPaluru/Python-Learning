# From a list numbers move Zero to the End.



list = [2, 0, 2, "manju",  12, 2, 4, 0, 8]
for i in list:
    if i == "manju":
        list.remove(i)
        list.append(i)

print(list)
list.append("hi")
print(list)