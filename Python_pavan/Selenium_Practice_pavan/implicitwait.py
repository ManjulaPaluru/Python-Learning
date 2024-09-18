import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
time.sleep(5)
searchbox = driver.find_element(By.NAME,"q")
searchbox.send_keys("selenium")
searchbox.submit()
driver.find_element(By.XPATH,"//div[@class='PZPZlf ssJ7i B5dxMb']").click()
print("success")
driver.close()