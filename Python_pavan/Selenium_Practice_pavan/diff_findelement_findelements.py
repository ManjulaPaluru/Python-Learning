import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
search_item = driver.find_element(By.ID,"small-searchterms")
search_item.send_keys("Apple Macbook")
driver.find_element(By.XPATH,"//button[text()='Search']").click()
print("search success")
footer_links = driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print("count of footer links: ",len(footer_links))
# accessing list of webelements by using index
print("first element ",footer_links[0].text)
print("first element ",footer_links[0].text)
# printing all the web elements by using for loop
for link in footer_links:
    print(link.text)
time.sleep(10)
driver.quit()