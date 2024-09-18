list = [1,2,3,4,5]
for i in range(0,len(list),1):
    # print(f"{i} => {list[i]}")
    if list[i] % 2 == 0:
        continue
    else:
        print(list[i], " ")
