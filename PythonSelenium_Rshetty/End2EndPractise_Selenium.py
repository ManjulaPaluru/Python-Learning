from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

phonename = []
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT,"Shop").click()
phoneList = driver.find_elements(By.XPATH,"//a/parent::h4")
for phone in phoneList:
    phonename.append(phone.text)
print(phonename)
if phonename == "Nokia Edge":
    phonename.find_element(By.XPATH,"[3]").click()
driver.find_element(By.XPATH,"(//button[@class='btn btn-info'])[3]").click()
driver.find_element(By.XPATH,"(//button[@class='btn btn-info'])[4]").click()
driver.find_element(By.XPATH,"(//button[@class='btn btn-info'])[1]").click()
checkoutItems = driver.find_element(By.XPATH,"//a[contains(text(),'Checkout')]")
#print(checkoutItems) -->printing web elements
print(checkoutItems.text)
driver.find_element(By.CSS_SELECTOR,".nav-link.btn.btn-primary").click()
driver.find_element(By.CSS_SELECTOR,".btn.btn-success").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver,20)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
successMessage = driver.find_element(By.CLASS_NAME,"alert-dismissible").text
print(successMessage)
expectedMessage = "Success! Thank you! Your order will be delivered in next few weeks :-)."
print(expectedMessage)
assert expectedMessage in successMessage
assert "Success! Thank you!" in successMessage
print("success")