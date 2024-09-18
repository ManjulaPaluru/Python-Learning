import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#Comparing the list of names which are displaying based on product

expectedList = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
actualList = []

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results =driver.find_elements(By.XPATH,"//div[@class='products']/div")
count= len(results)
print(count)
assert count > 0
# chaining of webelements
for product in results:
    actualList.append(product.find_element(By.XPATH,"h4").text)
    product.find_element(By.XPATH,"div/button").click()
assert expectedList == actualList
print(actualList)

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

# sum validation for total amount of 3 items
prices= driver.find_elements(By.XPATH,"//tbody/tr/td[5]")
sum= 0
for price in prices:
    sum = sum + int(price.text)
print(sum)

totalamount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum == totalamount

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
couponCodeMessage =  driver.find_element(By.CLASS_NAME,"promoInfo").text
print(couponCodeMessage)

# asserting total amount and total amount after adding discount
totalamountafterdiscount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert  totalamount > totalamountafterdiscount
print(totalamountafterdiscount)
allimages = driver.find_element(By.TAG_NAME,"img")




