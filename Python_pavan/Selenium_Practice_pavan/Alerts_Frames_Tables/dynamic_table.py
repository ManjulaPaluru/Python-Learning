from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")

driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
# # clicking Admin
# driver.find_element(By.XPATH,"//span[text()='Admin']").click()
# # clicking usermanagement
# driver.find_element(By.XPATH,"//span[@class='oxd-topbar-body-nav-tab-item'and text()='User Management ']").click()
# #clicking user
# driver.find_element(By.XPATH,"/a[text()='Users']").click()

# status = driver.find_elements(By.XPATH,"//div[text()='Enabled' or text()='Disabled']")
# print(len(status))
# enabled_records = driver.find_elements(By.XPATH,"//div[text()='Enabled']")
# print("records count for enabled status : ",len(enabled_records))
# disabled_records = driver.find_elements(By.XPATH,"//div[text()='Disabled']")
# print("records count for Disabledstatus : ",len(disabled_records))

row_count = driver.find_elements(By.XPATH,"//div[@class='oxd-table-body']/div/div")
print(len(row_count))



