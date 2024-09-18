import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("http://the-internet.herokuapp.com/windows")
# driver.find_element(By.XPATH,"//a[text()='Click Here']").click()
# windowid = driver.current_window_handle
# print("single window id :  ",windowid)

#
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(10)
driver.find_element(By.PARTIAL_LINK_TEXT,"OrangeHRM").click()
print("current window id ",driver.current_window_handle)
windows= driver.window_handles
print(windows)
for window in windows:
    driver.switch_to.window(window)
    if driver.title =="OrangeHRM":
        driver.close()



# driver.switch_to.window(windows[1])
# print(driver.title)
# driver.switch_to.window(windows[0])
# print(driver.title)


