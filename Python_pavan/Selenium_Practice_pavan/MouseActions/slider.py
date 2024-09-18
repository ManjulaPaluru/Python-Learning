import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
time.sleep(10)
min_slider = driver.find_element(By.XPATH,"//div/div/span[1]")
max_slider = driver.find_element(By.XPATH,"//div/div/span[2]")
# location is useful to print the location of slider
print("location of sliders before moving")
print(min_slider.location)
print(max_slider.location)

action = ActionChains(driver)
action.drag_and_drop_by_offset(min_slider,100,0).perform()
action.drag_and_drop_by_offset(max_slider,-39,0).perform()

print("location of sliders after moving")
print(min_slider.location)
print(max_slider.location)