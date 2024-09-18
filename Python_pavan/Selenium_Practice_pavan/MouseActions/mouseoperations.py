import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
driver.maximize_window()
time.sleep(5)
# driver.find_element(By.NAME,"username").send_keys("Admin")
# driver.find_element(By.NAME,"password").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
#
# #admin = driver.find_element(By.XPATH,"//span[text()='Admin']")
# user_management = driver.find_element(By.XPATH,"//span[text()='User Management ' and @class='oxd-topbar-body-nav-tab-item']")
# users = driver.find_element(By.XPATH,"//a[text()='Users']")
# # Creating ActionChains  class object
# action = ActionChains(driver)
# action.move_to_element(user_management).move_to_element(users).click().perform()

#
#drag & drop
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)
drag = driver.find_element(By.ID,"draggable")
drop = driver.find_element(By.ID,"droppable")
action = ActionChains(driver)
action.drag_and_drop(drag,drop).perform()

# driver.get("https://demoqa.com/menu/")
# driver.maximize_window()
# time.sleep(5)
# menu2 = driver.find_element(By.LINK_TEXT,"Main Item 2")
# #subitem = driver.find_element(By.LINK_TEXT,"Sub Item")
# sublist = driver.find_element(By.LINK_TEXT,"SUB SUB LIST »")
# action = ActionChains(driver)
# action.move_to_element(menu2).move_to_element(sublist).click().perform()
