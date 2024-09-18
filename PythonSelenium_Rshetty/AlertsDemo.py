import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
name="Manju"
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.current_url)
driver.find_element(By.XPATH,"//input[@id='name'][@class='inputs']").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert= driver.switch_to.alert
alerttext = alert.text
print(alerttext)
assert name in alerttext
alert.accept()
# conform
name1="confirm alert"
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='name'][@class='inputs']").send_keys(name1)
driver.find_element(By.ID,"confirmbtn").click()
alert = driver.switch_to.alert
alertconfirmtext= alert.text
print(alertconfirmtext)
time.sleep(2)
assert  name1 in alertconfirmtext
#alert.accept()
alert.dismiss()
