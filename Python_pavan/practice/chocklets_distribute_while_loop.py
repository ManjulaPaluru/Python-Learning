# i have 100 chocklets, i dont know the no of students. which loop is better to distribute.

chocolates = 100
student_num = 1
while(chocolates > 0):
    #print("Giving chocolate to student {} ".format(student_num))
    print(f"Giving chocolate to student {student_num}")
    chocolates -= 1
    student_num += 1


# using infinitive loop with break

chocolates = 50
student_num = 1
while True:
    if chocolates <=0:
        break
    print(f"Giving chocolate to student {student_num}")
    chocolates -= 1
    student_num += 1