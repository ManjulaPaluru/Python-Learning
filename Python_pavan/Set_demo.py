# set is collection of unordered, un indexed items.
myset = {"a","b","c"}
print(myset)
for i in myset:
    print(i)
print(len(myset))
myset.add("d")
print(myset)
myset.remove("a")
print(myset)
#myset.remove("f")  # key error will come when we try to remoe which is not available in set
myset.discard("f") # no error when e try to remove the element which is not in list.
#myset.clear() # clear method will clear the values from the set
print(myset)
#del myset # NameError: name 'myset' is not defined ,it will delete total set with values
print(myset)
# join 2 sets
myset1 ={1,2,3}
#myset3 =myset.union(myset1)
myset.update(myset1)
print(myset)

