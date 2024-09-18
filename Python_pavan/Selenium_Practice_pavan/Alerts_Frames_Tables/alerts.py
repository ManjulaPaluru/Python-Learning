from selenium import webdriver
from selenium.webdriver.common.by import By
# Accepting java script alert
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
myalert = driver.switch_to.alert
driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()

print(myalert.text)
myalert.accept()

# 2 Dissmising java sscript alert by selecting cancel option
driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
print(myalert.text)
myalert.dismiss()

#3 click for js prompt
driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
myalert.send_keys("I am manjula paluru")
myalert.accept()
actual_result = driver.find_element(By.XPATH,"//p[@id='result']")
print(actual_result.text)

