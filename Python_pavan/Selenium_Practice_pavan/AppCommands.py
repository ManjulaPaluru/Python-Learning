#1. Application commands :- get(),title,currenturl,pagesource
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# # page_title = driver.title
# # print(page_title)
# # currentrul = driver.current_url
# # print(currentrul)
# # pagesource = driver.page_source
# # print(pagesource)
#
#
# #2. Conditional commands like is_displayed(),is_enabled(),is_selected()
# username1= driver.find_element(By.XPATH,"//input[@name='username']")
# print("username is displayed " ,username1.is_displayed())
# password1 = driver.find_element(By.NAME,"password")
# print("password is field is enabled ",password1.is_enabled())
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
male_radiobutton = driver.find_element(By.XPATH,"//input[@id='gender-male']")
female_radiobutton = driver.find_element(By.XPATH,"//input[@id='gender-female']")
print("status of male radio button: " ,male_radiobutton.is_selected())
print("status of female radio button ",female_radiobutton.is_selected())
male_radiobutton.click()
print("status of male radio button after select: ",male_radiobutton.is_selected())
print("status of female radio button ",female_radiobutton.is_selected())
driver.quit()