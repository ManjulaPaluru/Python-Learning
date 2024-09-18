import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://text-compare.com/")
driver.maximize_window()
driver.implicitly_wait(5)
input1 = driver.find_element(By.ID,"inputText1")
input2 = driver.find_element(By.ID,"inputText2")
action = ActionChains(driver)
# ctrl+A select the text
input1.send_keys("my name is manjula")
print(input1.get_attribute("value"))
action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
# ctrl+ c copy the text
action.key_down(Keys.CONTROL) # pressing control key
action.send_keys("c")
action.key_up(Keys.CONTROL) # releasing the key
action.perform()

# move to next text box(input2) by using tab key
action.send_keys(Keys.TAB).perform()

# paste the text in input2 text box
action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
print(input2.text)
print(input2.get_attribute("value"))