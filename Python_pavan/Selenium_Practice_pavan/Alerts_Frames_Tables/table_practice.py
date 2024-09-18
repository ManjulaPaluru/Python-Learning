from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/?m=1")
# table_data = driver.find_elements(By.XPATH,"//table[@name='BookTable']//td")
# print(len(table_data))
# for data in table_data:
#     print(data.text)

rows = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
print(len(rows))
for row in rows:
    print(row.text)
row_5th = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[5]")
for i in row_5th:

    print("printing 5 th row :",i.text)
