import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[text()='Register']").click()
driver.find_elements(By.ID, "firstName").send_keys("tester1")
driver.find_elements(By.ID, "firstName").send_keys("paluru")
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("tester1@gmail.com")
driver.find_element(By.ID, "userMobile").send_keys(1234567890)
driver.find_element(By.XPATH, "//input[@value='userMobile']").click()
time.sleep(5)