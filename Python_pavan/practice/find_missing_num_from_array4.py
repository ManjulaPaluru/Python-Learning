#ex: [1,2,4,5,6,7] find the missing no from array/list
list1 = [1,2,4,5,6,7]
sum1 = sum(list1)
print(sum1)
sum2 =0
for i in range(1,8): # range function will start with starting value, end value is  end -1
    sum2 = sum2+i
print("sum2",sum2)
missing_no = sum2 - sum1
print(missing_no)

# summation method
n = list1[-1] # -1 represent the last element 7
print(n)
sum_of_natural_no = n * (n+1)//2
print(sum_of_natural_no)
sum_array = sum(list1)
missing_no = sum_of_natural_no - sum_array
print(missing_no)


# Xor method


