import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
time.sleep(10)
driver.switch_to.frame("iframeResult")
field1 = driver.find_element(By.ID,"field1")
field1.clear()
field1.send_keys("manjula")
field2 = driver.find_element(By.ID,"field2")
copy_text = driver.find_element(By.XPATH,"//button[text()='Copy Text']")
action =ActionChains(driver)
action.double_click(copy_text).perform()
print(field2.get_attribute("value"))