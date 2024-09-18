# Example 1: Write a program to find the ocmmon letters from given two strings
str1 = input("enter the first string: ")
str2 = input("enter t he second string: ")
s1=set(str1)
s2=set(str2)
common_letters = s1 & s2
print("common letters from two strings: ", common_letters)


# Approach 2 using intersection method
common = set(str1).intersection(set(str2))
print("common",common)
