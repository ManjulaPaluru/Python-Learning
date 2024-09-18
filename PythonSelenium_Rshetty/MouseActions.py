import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.current_url)
# we need to create action calss object for performing mouse actions.
action  =  ActionChains(driver)
driver.implicitly_wait(10)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).click().perform()
print("mouse operations are done")
action.click_and_hold
action.drag_and_drop()
action.double_click()
action.drag_and_drop_by_offset()
action.key_down()
action.key_up()
action.move_by_offset()
action.move_to_element_with_offset()
action.scroll_to_element()
action.pause()
action.release()