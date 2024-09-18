import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.current_url)
# Raido button
radioButtons = driver.find_elements(By.XPATH,"//input[@name='radioButton']")
print(len(radioButtons))
for radiobutton in radioButtons:
    time.sleep(2)
    if radiobutton.get_attribute("value") == "radio2":
        radiobutton.click()
        break

# suggestion class example
driver.find_element(By.ID,"autocomplete").send_keys("India")
time.sleep(2)
driver.find_element(By.ID,"autocomplete").send_keys("United States")
time.sleep(2)

# Static dropdown select clause
dropdown = Select(driver.find_element(By.ID,"dropdown-class-example"))
time.sleep(2)
dropdown.select_by_index(2)
dropdown.select_by_visible_text("Option1")
assert driver.find_element(By.ID,"dropdown-class-example").get_attribute("value") == "option1"

# selecting checkboxes
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))
#for checkbox in checkboxes:
#   time.sleep(2)
#   if checkbox.get_attribute("value") == "Option2":
#       time.sleep(2)
#       checkbox.click()
#       assert checkbox.is_selected()
#       break

# select check box by using id
#driver.find_element(By.ID, "checkBoxOption2").click()

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()


#checkboxes = driver.find_elements(By.CSS_SELECTOR,".right-align")
#checkboxes[2].click()
#time.sleep(3)
#assert checkboxes[2].is_selected()