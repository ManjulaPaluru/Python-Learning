import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(10)
#multiple frames are in webpage
driver.get("http://the-internet.herokuapp.com/frames")

# driver.find_element(By.XPATH,"//a[text()='Nested Frames']").click()
# driver.switch_to.frame("frame-left")
# driver.switch_to.default_content()
#
# driver.switch_to.frame("frame-middle")
# driver.switch_to.default_content()
# driver.switch_to.frame("frame-bottom")
# driver.switch_to.default_content()


# single frame on webpage
# driver.get("https://demo.automationtesting.in/Frames.html")
# driver.find_element(By.XPATH,"//a[text()='Single Iframe ']").click()
# driver.switch_to.frame("SingleFrame")
# textbox = (driver.find_element(By.XPATH,"//input[@type='text']"))
# textbox.send_keys("manjula")
# time.sleep(10)
# print(textbox.get_attribute("value"))
