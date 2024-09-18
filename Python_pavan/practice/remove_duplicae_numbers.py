#4 remove duplicate letters form given string
def remove_duplicate(input_string):
    new_string = " "
    for i in input_string:
        if i in new_string:
            continue
        else:
            new_string = new_string+i
    return new_string

input_string = "hiiiiii"
result = remove_duplicate(input_string)
print(result)




