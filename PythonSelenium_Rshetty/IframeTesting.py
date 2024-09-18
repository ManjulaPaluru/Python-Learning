from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
#driver.find_element(By.ID,"tinymce").clear()
#driver.find_element(By.ID,"tinymce").sendkeys("adding automation text")
driver.switch_to.default_content()
text = driver.find_element(By.XPATH,"//div/h3").text
print(text)