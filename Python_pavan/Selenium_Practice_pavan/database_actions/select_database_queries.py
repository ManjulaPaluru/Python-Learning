import mysql.connector


try:
    connection = mysql.connector.connect(host = "localhost",port=3306,user="root",password="root$1234",database= "Selenium_testing")
    curs = connection.cursor() #crete a cursor which is temporary memory
    curs.execute("Select * from employee")
    for row in curs:
        print(row[0],row[1],row[2])

    connection.close() #closing the connection
except:
    print("connection unsuccessfull")

print("finished")