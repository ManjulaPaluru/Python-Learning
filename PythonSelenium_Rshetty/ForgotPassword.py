import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
#
#driver.find_element(By.LINK_TEXT, "Forgot password?").click()
#driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("ab@c.gom")
#driver.find_element(By.ID,"userPassword").send_keys("Pwd$1234")
#driver.find_element(By.ID, "confirmPassword").send_keys("Pwd$1234")
#driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()

time.sleep(5)