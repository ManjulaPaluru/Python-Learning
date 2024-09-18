import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pythonBasics_Rshetty import List

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print("Current url:" ,  driver.current_url)
driver.find_element(By.NAME, "name").send_keys("Manjula")
driver.find_element(By.NAME, "email").send_keys("manjula.pu@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Pwd$123")
driver.find_element(By.ID, "exampleCheck1").click()
# static dropdown
dropdown = Select(driver.find_element(By.XPATH,"//select[@id='exampleFormControlSelect1']"))
dropdown.select_by_index(1)
time.sleep(10)
dropdown.select_by_visible_text("Male")
driver.find_element(By.XPATH,"//input[@id='inlineRadio1']").click()
driver.find_element(By.XPATH,"//input[@class='form-control' and @name='bday']").click()
driver.find_element(By.XPATH,"(//input[@type='text' and @name='name'])[2]").send_keys("hiiiiii")
driver.find_element(By.CSS_SELECTOR,"input[value='Submit']").click()
message = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
print(message)
assert "Success" in message

