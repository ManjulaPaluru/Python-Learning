from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
windowsopened = driver.window_handles
driver.switch_to.window(windowsopened[1])
emailid = driver.find_element(By.XPATH,"//p[@class='im-para red']//a").text
print(emailid)
driver.switch_to.window(windowsopened[0])
driver.find_element(By.ID,"username").send_keys(emailid)
driver.find_element(By.ID,"signInBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)


