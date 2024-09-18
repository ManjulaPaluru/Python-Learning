import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# country
driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
country_list = driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(country_list))
for country in country_list:
    print(country.text)
    if country.text == "Iceland":
        country.click()
        break

time.sleep(10)