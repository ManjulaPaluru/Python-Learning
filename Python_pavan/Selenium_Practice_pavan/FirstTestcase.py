
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service(executable_path="/Users/ssaguturu/workspace/softwares/drivers/chromedriver")
#service_obj = Service(executable_path="/Users/ssaguturu/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
#driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
actual_title = driver.title
expect_title = "OrangeHRM"
if actual_title == expect_title:

    print(" Login test pass")
else:
    print("login test fail")
links = driver.find_elements(By.TAG_NAME,"a")
print("total no of links on webpage",len(links))
driver.close()