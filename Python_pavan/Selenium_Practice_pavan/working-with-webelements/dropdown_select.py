import time
from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")


# static dropdown using Select class
# countrydropdown = Select(driver.find_element(By.ID,"country"))
# # countrydropdown.select_by_visible_text("Germany")
# # countrydropdown.select_by_index(2)
# # countrydropdown.select_by_value("china")

# getting all opetions and printing without using select class
all_options = driver.find_elements(By.XPATH,"//select[@id='country']/option")
print(len(all_options))
for opt in all_options:
    print(opt.text)
    if opt.text=="Canada":
        opt.click()

#color_options = Select(driver.find_element(By.XPATH,"//select[@id='colors']"))
# time.sleep(10)
# color_options.select_by_index(0)
# # color_options.select_by_visible_text("Red")
# # color_options.select_by_value("blue")

# selecting color drop down without using select class
color_opt = driver.find_elements(By.XPATH,"//select[@id='colors']/option ")
print(len(color_opt))
for color in color_opt:
    print(color.text)
    if color.text == "Red":
        color.click()
# selecting color from drop down with using select class
color_opt = Select(driver.find_element(By.XPATH,"//select[@id='colors']"))
for opt in color_opt:
    print(opt.text)
    if opt.text == "Yellow":
        opt.click()



