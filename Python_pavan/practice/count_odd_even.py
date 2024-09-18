#3 write a program to count odd and event no from given array
input = [1, 2,3,4,5,6,7,8,9]
even_count = 0
odd_count = 0
for i in input:
    if i % 2 == 0:

        even_count= even_count + 1
    else:

        odd_count =  odd_count + 1
print("even numbers count")
print(even_count)
print("odd numbers count")
print(odd_count)