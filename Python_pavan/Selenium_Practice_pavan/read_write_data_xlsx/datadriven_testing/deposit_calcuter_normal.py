import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
expected_cd= "$39,304.52"
driver.get("https://www.cit.com/cit-bank/resources/calculators/certificate-of-deposit-calculator")
driver.implicitly_wait(20)
# initial deposit amount
driver.find_element(By.ID,"mat-input-0").clear() # clear the field first
driver.find_element(By.ID,"mat-input-0").send_keys("$35000")# entering the value
#length of cd-months
driver.find_element(By.ID,"mat-input-1").clear()
driver.find_element(By.ID,"mat-input-1").send_keys("20")
# interest rate
driver.find_element(By.XPATH,"//input[@id='mat-input-2']").clear()
driver.find_element(By.XPATH,"//input[@id='mat-input-2']").send_keys("7")
time.sleep(10)
# clicking arrow mark
driver.find_element(By.XPATH,"//div[@class='mat-select-arrow-wrapper ng-tns-c109-4']").click()
# get all mat options
m_options = driver.find_elements(By.XPATH,"//span[@class='mat-option-text']")
print(len(m_options))
for option in m_options:
    print(option.text)
    if option.text == "Compounded Semi-Annually":
        option.click()
selected_value = driver.find_element(By.XPATH,"//mat-select[@id='mat-select-0']")
print("selected value: ",selected_value.text)
# click on lets run the numbers
driver.find_element(By.XPATH,"//button[@id='CIT-chart-submit']").click()

#Validation comparing expected vs actual value
actual_cd = driver.find_element(By.XPATH,"//span[@id='displayTotalValue']").text

if expected_cd==actual_cd:
    print("pass")
else:
    print("fail")
