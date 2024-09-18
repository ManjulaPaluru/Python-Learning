from selenium import webdriver

chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_argument("headless")
chromeoptions.add_argument("--ignore-certification-errors")
chromeoptions.add_argument("--start-maximized")
chromeoptions.add_argument("disable-popup-blocking")
driver = webdriver.Chrome(options=chromeoptions)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
print(driver.title)
