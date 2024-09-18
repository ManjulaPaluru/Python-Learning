import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.ID,"dob").click()
all_months_options = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
print(len(all_months_options.options))
#all_months_options.select_by_index(1)
time.sleep(5)
all_months_options.select_by_visible_text("Jun")


years = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
time.sleep(5)
print(len(years.options))
years.select_by_visible_text("2020")
year_text = driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']")
year_text.get_attribute("value")

all_dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for date in all_dates:
    if date.text == "25":
        date.click()
        break


