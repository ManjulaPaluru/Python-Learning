# given string "good morning" write the program that output should be index of each character is dictonary format.
'''Explanation
The function string_to_index_dict takes a string input_string as an argument.
It initializes an empty dictionary index_dict.
It then iterates over the string using enumerate, which provides both the index and the character at that index.
For each character, it checks if the character is already in the dictionary.
If it is, it appends the current index to the list of indices for that character.
If it is not, it creates a new entry in the dictionary with the character as the key and a list containing the current index as the value.
Finally, it returns the dictionary.'''

def string_to_index_dict(input_string):
   index_dict= {}
   for index, char in enumerate(input_string):
      if char in index_dict:
         index_dict[char].append(index)
      else:
         index_dict[char] = [index]
   return index_dict

result = string_to_index_dict("Good Morning")
print(result)

# String to dictionary without using enumerate method
str = "Manjula Paluru"
dict = {}
index =0
for char in str:
   if char in dict:
      dict[char].append(index)
   else:
      dict[char]=[index]
   index = index +1
print(dict)



list =[]
list.insert(0,1)
list.insert(1,2)
list.insert(2,3)
list.insert(1,6)
print(list)
print(len(list))




