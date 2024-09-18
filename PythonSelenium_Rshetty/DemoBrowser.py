import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#chrome driver service using for fast purpose if vpn connetion is enabled, and
# some compines are not allowed to download from net for that we need to download later version of (related to out browser)
#chrome driver and give that path to service class.

#service_obj = Service("/Users/ssaguturu/workspace/softwares/chromedriver_mac_arm64/chromedriver")
#driver = webdriver.Chrome(service=service_obj)

#chromedriverpath= '/Users/ssaguturu/Downloads/chromedriver_mac_arm64 (1)/chromedriver'
#driver = webdriver.Chrome(executable_path = chromedriverpath)
#driver = webdriver.Firefox()
#driver = webdriver.Chrome()
driver = webdriver.Safari()
driver.get("https://www.rahulshettyacademy.com")
driver.maximize_window()
title= driver.title
print(title)
print(driver.current_url)
print(driver.page_source)
















time.sleep(2)