import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[text()='OrangeHRM, Inc']").click()
time.sleep(15)

driver.close()
#driver.quit()