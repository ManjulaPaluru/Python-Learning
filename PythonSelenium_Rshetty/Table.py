from selenium import webdriver
from selenium.webdriver.common.by import By
browserssortedveggilist = []
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
print("fruit name click")
veggieList = driver.find_elements(By.XPATH,"//tr/td[1]")
print(veggieList)
for ele in veggieList:
    browserssortedveggilist.append(ele.text)
browserssortedveggilist = browserssortedveggilist.copy()
print(browserssortedveggilist)
sortdveggilist = browserssortedveggilist.sort()
print(sortdveggilist)
if browserssortedveggilist == sortdveggilist:
    print("same")
else:
    print("not same")

#logic build
# get all list of  veggies--veggie list
# sort the veggie list -- sorted veggie list
# compare both list

