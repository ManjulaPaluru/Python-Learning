# write a program to find the words from given string
#ex: Hi this is python program

str = input("enter the string: ")
dic= {}
words= str.split()
print(words)
for word in words:
    if word not in dic.keys():
        dic[word] = 1
    else:
        dic[word]= dic[word]+1
print(dic)
print(len(words))

# APPROACH 2
str = input("enter the string: ")
dic= {}
words= str.split()
for word in words:
    dic[word]=dic.get(word,0)+1
print(dic)

