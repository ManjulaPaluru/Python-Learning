import mysql.connector


insert_query = "insert into Student values(11, 'manjup',250)"
update_query = "update Student set sname ='automation' where sno=1"

try:
    connection = mysql.connector.connect(host = "localhost",port=3306,user="root",password="root$1234",database= "Selenium_testing")
    curs = connection.cursor() #crete a cursor which is temporary memory
    #curs.execute(insert_query) #execute the sql command through cursor
    #curs.execute("create table employee(eno int(5), ename varchar(10),sal int(10))")
    # curs.execute("insert into employee values (1,'manju',5000)")
    # curs.execute("insert into employee values (11,'anju',15000)")
    #curs.execute("insert into employee values (111,'manju p',115000)")
    # curs.execute("insert into employee values (1111,'manju s',1115000)")
    curs.execute(update_query)
    connection.commit() # commit the transcation
    connection.close() #closing the connection
except:
    print("connection unsuccessfull")

print("finished")