from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://snapdeal.com")
driver.get("https://amazion.com")
driver.back()
print("after backing expecting snapdeal",driver.title)
driver.forward()
print("after forward expecting amazion",driver.title)
driver.refresh()
