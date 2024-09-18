from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

# below code while opening second url it will replace the first tab which first url is opened. for avoiding that in selenium 3 we are using keyboard commands ctrl+return
driver= webdriver.Chrome()
# driver.get("https://demo.nopcommerce.com")
# register_link = Keys.CONTROL+Keys.RETURN
# driver.implicitly_wait(10)
# driver.find_element(By.LINK_TEXT,"Register").send_keys(register_link)
# driver.implicitly_wait(10)

# in selenium 4 if we want to open second url or link in separate tab we can do, opens a new tab and switch to new tap
# driver.get("https://demo.nopcommerce.com")
# driver.switch_to.new_window('tab')
# driver.get("https://www.dummyticket.com")
# How to open new browser window in  selenium 4 without reloading the previous window for second url or link
driver.get("https://demo.nopcommerce.com")
driver.switch_to.new_window('window')
driver.get("https://www.dummyticket.com")
driver.get_cookies()

