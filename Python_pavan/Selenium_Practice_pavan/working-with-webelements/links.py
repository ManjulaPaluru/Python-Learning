from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
# click on link by using link text and xpath
link = driver.find_element(By.LINK_TEXT,"Digital downloads")
#link = driver.find_element(By.PARTIAL_LINK_TEXT,"Digital")
print(link)
# find no of links in a webpage
#links = driver.find_elements(By.TAG_NAME,"a")
links = driver.find_elements(By.XPATH,"//a")
for link in links:
    print(link.text)