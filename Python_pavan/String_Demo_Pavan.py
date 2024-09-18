# different ways of creating  string  variables
s = "welcome"
s = 'Welcome'
s = str("Welocme")
s = str('Welcome')
# creating empty string variables
s = str()
s = ""
s = ''
# Mutable:- We can change the values of the variable anytime
# Immutable:-  We can't change the value of the variable
# Strings are immutable
#
str1 ="welcome"
print(id(str1))   #4367652576
str1 = str1 +"python"
print(id(str1))   #4367897712
# slicing operator
#[start:end:step]
str = "welcome"
print(str[1:3])  #el
print(str[:6])   #welcom
print(str[2:])   #lcome
print(str[::])   #welcome
print(str[1:-1])  #elcom
print(str[1:-3])  #elc
# ord() function will return asci no of the character.and  chr() function will return character of number.
print(ord('A'))  #65
print(chr(65))   #A
# max() min() len()
print(max("abc"))  #c
print(min("manjula")) #a
print(len("1234")) #4
# in , not in operators in strings
s="welcome"
print("come" in s)  #True
print("manju" in s)  # False
print ("manju" not in s) #True
print("come" not in s) #False
print("***************")
# String comparing
s ="welcome"
s1 ="welcome"
print(s == s1) #True
print(s != s1) # False
print(s.isalnum())
print(s.isalpha())
print(s.isdigit()) #false
print(" ".isspace())
print("Fist number".isidentifier())
print(s.islower())
print("WELCOME".isupper())
print("***************")
# Searching for substring
s = "welcome to python"
print(s.startswith("wel")) #true
print(s.endswith("me")) # false
print(s.find("come")) #3
print(s.find("manju")) # -1 not found
print(s.count("o")) #3
print(s.count("t")) #2
# CONVERTING STRING
s = "manjula paluru"
s1 = s.capitalize()
print(s1) #Manjula Paluru
s1 =s.swapcase()
print(s1) #MANJULA PALURU
s1 =s.replace("manjula" ,"hi")
print(s1) #hi paluru
s ="M$12jula"
s1 =s.replace("$","*")
print(s1) #M*12jula
# example how to reverse a string
print("*********")
s = "manjula"
temp = " "
for i in s:
    temp = i+temp
print(temp)
# Method 2 using slicing operator
print(s[::-1]) #alujnam
# reversing number using slicing operator
s = "1234567"
print(s[::-1]) #7654321
# reversing no using for loop
s = "1234567"
temp =" "
for i in s:
    temp = i+temp
print(temp) #7654321



