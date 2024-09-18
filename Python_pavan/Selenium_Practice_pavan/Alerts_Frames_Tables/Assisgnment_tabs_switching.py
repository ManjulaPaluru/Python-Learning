import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

searchbox= (driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input"))
searchbox.send_keys("selenium")
driver.find_element(By.XPATH,"//input[@type='submit' and @class='wikipedia-search-button']").submit()
time.sleep(5)
search_results = driver.find_elements(By.XPATH,"//div[@id='wikipedia-search-result-link']/a")
print(len(search_results))
print("printing and clicking on links...............")
for result in search_results:
    print(result.text)
    result.click()
#After opening all the pages, capture windowid's
all_windows = driver.window_handles
print("Switching to each browser window and getting the titles........")
for window in all_windows:
    time.sleep(5)
    driver.switch_to.window(window)
    print(driver.title)
for window in all_windows:
    if driver.title == "Selenium":
        driver.close()

#driver.quit()