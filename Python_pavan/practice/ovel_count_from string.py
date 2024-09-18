# count ovels from given string
string1 = "aeiou"
ovel_count =0
conso_count =0
for i in string1:

    if i .__contains__('a' or 'e' or 'i' or 'o' or 'u'):
        ovel_count +=1
    else:
        conso_count +=1



print(ovel_count)
print(conso_count)