import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
brokenLink_count = 0
ValidLink_count = 0
driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
alllinks = driver.find_elements(By.TAG_NAME,"a")

for link in alllinks:
    url = link.get_attribute('href')
    res = requests.head(url)
    if res.status_code >= 400:
        print(url, "is Broken link")
        brokenLink_count +=1
    else:
        print(url, "is valid link")
        ValidLink_count +=1

print("All links from webpage ",len(alllinks))
print("count of all valid links: ",ValidLink_count)
print("count of all broken links: ", brokenLink_count)