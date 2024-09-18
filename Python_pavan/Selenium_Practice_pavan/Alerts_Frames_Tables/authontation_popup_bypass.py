
# handling Authentation popups: By injecting username and password to url to by pass the authentation popup.
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
time.sleep(5)
driver.maximize_window()
# #driver.get("http://the-internet.herokuapp.com/basic_auth")
# driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")


# Broken Images
driver.get("http://the-internet.herokuapp.com/")
# clicking on broken images link
driver.find_element(By.XPATH,"//a[text()='Broken Images']").click()
images = driver.find_elements(By.XPATH,"//div[@class='example']/img")
print(len(images))
count =0
for image in images:
    url= image.get_attribute("src")
    res= requests.head(url)
    if res.status_code >= 400:
        print(url,"Broken image")

        count += 1
    else:
        print(url, "valid image")
