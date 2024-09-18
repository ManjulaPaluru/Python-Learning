import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
# Broken Images
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
#driver.find_element(By.XPATH,"//iframe[@id='frame-one796456169']")
driver.switch_to.frame("frame-one796456169")
driver.find_element(By.NAME,"RESULT_TextField-0").send_keys("manjula")
# # select ing radio button
# genders = driver.find_elements(By.XPATH,"//table/tbody/tr/td/label")
# print(genders)
# time.sleep(2)
# for gender in genders:
##     print(gender.text)
#     if gender.text == "Female":
#         gender.click()
#         print("female selected")

# selecting radi button gender
# we can use '.' instead of text() method 
driver.find_element(By.XPATH,"//label[.='Male']")
time.sleep(10)
# jobs= driver.find_elements(By.ID,"RESULT_RadioButton-3")
# for job in jobs:
#     print(len(jobs))
#     print(job.text)
#     if job.text == "Manager":
#         job.click()
driver.find_element(By.NAME,"Submit").click()
driver.switch_to.default_content()