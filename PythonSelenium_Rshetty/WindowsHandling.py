
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
text = driver.find_element(By.TAG_NAME, "h3").text
print(text)
driver.find_element(By.LINK_TEXT,"Click Here").click()
# for navigating to child window, we have method in selenium called window_handles,
# by using that we can get all opened windows, through index positions we can access the child window or parent window.

windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
text = driver.find_element(By.TAG_NAME, "h3").text
print(text)
driver.close()
# navigating back to parent window
driver.switch_to.window(windowsOpened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
print("assertion is over")