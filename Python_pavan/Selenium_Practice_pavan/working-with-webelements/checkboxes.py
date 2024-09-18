import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
# 1. select single check box
# checkbox = (driver.find_element(By.ID,"saturday"))
# checkbox.click()
# print("check box is select: ",checkbox.is_selected())
# 2. selecting Multiple checkboxes
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))
# 3. selecting check boxed by weekname
# for checkbox in checkboxes:
#     weekname= checkbox.__getattribute__('id')
#     if weekname =='Monday' or 'Sunday':
#         checkbox.click()
#
# 4. select and unselect all checkboxes
# for checkbox in checkboxes:
#     checkbox.click()
# for checkbox in checkboxes:
#     if checkbox.is_selected():
#         checkbox.click()
#5 selecting last 2 checkboxed
for checkbox in range(len(checkboxes)-2,len(checkboxes)):
    checkboxes[checkbox].click()
# 6 selecting first 2 checkboxes
for checkbox in range(len(checkboxes)):
    if checkbox < 2:
        checkboxes[checkbox].click()

driver.close()