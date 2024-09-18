#prime no is greater than 1. prime no is which no is divided by 2 and modulo devision is not a zero.
num = 6
if num > 1:
    if (num % 2) == 0:
        print("not a prime no")
    else:
        print("prime no")

# program for displaying a prime number with in an interval are range of the numbers
# first take the 2 variables for low and upper ranges lower and upper
# iterate the value using for loop starting from lower to upper  increment by 1
# condition check number should be >1
# write inner for loop for iterating the values initilize i value to 2 and increment through num
# check condition num modlo by i equals to 0
# break the loop otherwise print the num.

lower = 100
upper = 200
for num in range(lower, upper, +1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
          print(num)







