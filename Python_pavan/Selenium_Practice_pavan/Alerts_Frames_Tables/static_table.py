from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
#1.  total no of rows
# total no of columns
len_rows = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
# print(len(len_rows))
# len_columns = driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
# print(len(len_columns))
# #2. Read data from specefic row and column
# data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[2]/td[1]").text
# print(data)
#
# # Read data from specific row
# row_data = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[2]/td")
# print(len(row_data))
# for data in row_data:
#     print(data.text)
# # print data from all rows and column data
# for row in range(2,len(len_rows)+1):
#     for col in range(1,len(len_columns)+1):
#         data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(row)+"]/td["+str(col)+"]").text
#         print(data, end='    ')
#     print()
# # print data from all rows and columns
# all_row_col_data = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/td")
# for data1 in all_row_col_data:
#         print(data1.text)
# print the data based on condition (list book  name baseed on author name is Mukesh

#
for row in range(2,len(len_rows)+1):
    authorname= driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[2]").text
    if authorname=="Mukesh":
        bookname = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[1]").text
        price = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(row)+"]/td[4]").text
        print(bookname,"  ",authorname,"  ",price)



driver.close()


