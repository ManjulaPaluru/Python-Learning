# open the  text file and read as a list
# reverse the list
#write  the list in to file

# with open("test.txt", 'w') as writer:
#    writer.writelines("manju")

line_1 = ('anju\n',
          'paluru\n'
          'akhil\n')

with open("test.txt", 'w') as writer:
    for line in line_1:
        writer.write(line)
    writer.writelines("this is my second line.\nsecond lline.\nthird line\n")
with open("test.txt", 'r' ) as file:
    content= file.readlines()
    for line in content:
        print(line)
with open("test.txt", 'a') as file:
    file.write("thank you very much.\nyou are so wonderful")

