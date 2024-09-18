#raise out own exception
i = 10
if i == 10:
    print("no exception")
else:
     raise Exception("i vale is not equal to specified no")

# assert
assert (i == 10)
print("assertion pass do to i value is as defined")



# try and except block for handling exception

try:
    c = 1/0
except Exception as e:
    print(e)
finally:
    print("closing all database connections")

# try with else cluase
def reciprocal(num1):
    try:
        reci = 1 / num1
    except Exception as e:
        print (e)
    else:
        print(reci)
reciprocal(2)
reciprocal(0)





