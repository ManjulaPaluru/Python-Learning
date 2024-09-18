import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.implicitly_wait(20)
driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"input#pass").send_keys("test123")
# #driver.find_element(By.XPATH,"//button[@id='loginbutton' and @name='login']").click()
driver.find_element(By.LINK_TEXT,"Create new account").click()
# driver.find_element(By.NAME,"firstname").send_keys("test_100_firstname")
# driver.find_element(By.NAME,"lastname").send_keys("test_100_lastname")
# #driver.find_element(By.XPATH,"//input[@id='u_0_g_QW']").send_keys(1234567890)
# driver.find_element(By.ID,"password_step_input").send_keys("test$123")
# driver.find_element(By.XPATH,"(//label[@class='_58mt'])[1]").click()
months = Select(driver.find_element(By.ID,"month"))
time.sleep(20)
months.select_by_index(2)
months.select_by_visible_text("Aug")


