from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.XPATH,"(//div[@id='opc-product-selection']/ul/li/label/input)[4]").click()
# name
driver.find_element(By.ID,"travname").send_keys("Manjula")
#last name
driver.find_element(By.ID,"travlastname").send_keys("paluru")
#radio button
driver.find_element(By.ID,"sex_2").click()
# checkbox
driver.find_element(By.XPATH,"//input[@type='checkbox' and @id='addmorepax']").click()
# trip type
trip_types = driver.find_elements(By.XPATH,"//span/input[@type='radio' and @name='traveltype']")
for trip_type in trip_types:

    if trip_type.text =="RoundTrip":
        trip_type.click()
#from city/origin
driver.find_element(By.NAME,"fromcity").send_keys("SFO")
driver.find_element(By.NAME,"tocity").send_keys("Log Angles")
driver.find_element(By.ID,"departon").send_keys("23/07/2024")
#return date
#driver.find_element(By.ID,"returndate").send_keys("25/07/2024")
driver.find_element(By.XPATH,"//span[@id='select2-reasondummy-container']").click()
visa_application = driver.find_elements(By.XPATH,"//span[@class='select2-results']/ul/li")

for visa_type in visa_application:

    if visa_type.text == "Visa extension":
        visa_type.click()


