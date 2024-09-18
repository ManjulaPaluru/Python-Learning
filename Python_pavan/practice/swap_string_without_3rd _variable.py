s1 = "hello"
s2 = "world"
s1,s2 = s2,s1 # tple unpacking
print(s1)
print(s2)

# Initialize the strings
str1 = "hello"
str2 = "world"

# Swap using string concatenation
str1 = str1 + str2  # str1 now holds "helloworld"
str2 = str1[:len(str1) - len(str2)]  # str2 now holds "hello"
str1 = str1[len(str2):]  # str1 now holds "world"

print("str1:", str1)
print("str2:", str2)