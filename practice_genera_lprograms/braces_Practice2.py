from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//a[@aria-label='Google apps']").click()



