list = [1,2,2,2,3,3,3]
find_ele = 2
count =0
new_list =  []
for i in list:

    if i in new_list:
        count += 1
    else:
        new_list.append(i)


print(count)
print(new_list)