
file = open("test.txt")
#print(file.read())
#print(file.read(15))
#line = file.readline()
#while line!="":
#   print(line)
#   line = file.readline()
# using readline method with while loop for reading line by line and  printing values
#line= file.readline()
#while line!="":
#    print(line)
#    line=file.readline()

# using readlines method with for loop for reading all lines and
# it will display list of values, by using for loop we can read the values on by one and print values

for line1 in file.readlines():
    print(line1)


file.close()