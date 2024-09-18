import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0) # switch to frame
driver.implicitly_wait(10)
date = driver.find_element(By.ID,"datepicker").send_keys("07/15/2024")
selecteddate = driver.find_element(By.XPATH,"//input[@type='text' and @class='hasDatepicker']")
print(selecteddate.get_attribute("value"))

expected_month = "March"
expected_year = "2025"
expected_date = "23"

while True:
    month = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    year = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if month == expected_month and year == expected_year:
        break

    else:
        #driver.find_element(By.XPATH, "//span[text()='Prev']").click()  # previous date

        driver.find_element(By.XPATH,"//span[text()='Next']").click() # next date
#select dates
dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for date in dates:
    if date.text == expected_date:
        date.click()
        time.sleep(10)
        print(selecteddate.get_attribute("value"))
        break
