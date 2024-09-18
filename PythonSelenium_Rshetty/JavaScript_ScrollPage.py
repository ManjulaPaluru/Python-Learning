from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certification-errors")

driver =webdriver.Chrome(options=chrome_options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy")
driver.execute_script("window.scrollBy(0,700);")
driver.execute_script("window.scrollBy(0,document.body.scrollByHight);")
#driver.get_screenshot_as_file("screen.png")
driver.get_screenshot_as_png()