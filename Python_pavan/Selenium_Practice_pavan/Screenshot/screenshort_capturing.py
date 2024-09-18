from selenium import webdriver
import os

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.implicitly_wait(10)
#driver.save_screenshot("/Users/ssaguturu/PycharmProjects/pythonProject/Python_pavan/Selenium_Practice_pavan/Screenshot/homepage.png")
# for avoiding writing  full path we need to import os module and use the predefined method getcwd() get current working directory
driver.save_screenshot(os.getcwd()+"/homepage.png")
driver.get_screenshot_as_file(os.getcwd()+"/homepage1.png")
# if we want save as asecuried files use below methods for saving screenshot
#driver.get_screenshot_as_png()
#driver.get_screenshot_as_base64()

driver.quit()