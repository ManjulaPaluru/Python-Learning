
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

# # X path of self Node
# text_message = driver.find_element(By.XPATH,"//a[contains(text(),'Abbott India Ltd.')]/self::a").text
# print(text_message)
# driver.close()

# Parent no x path
# parent_text_message = driver.find_element(By.XPATH,"//a[contains(text(),'Abbott India Ltd.')]/parent::td").text
# print(parent_text_message)

#child node x path
# row_data = driver.find_elements(By.XPATH,"//a[contains(text(),'Abbott India Ltd.')]/ancestor::tr/child::td")
# print(len(row_data))
# print(row_data)
# Ancestor
# text_message = driver.find_element(By.XPATH,"//a[contains(text(),'Abbott India Ltd.')]/ancestor::tr").text
# print(text_message)
# following siblings
f_siblings= driver.find_elements(By.XPATH,"//a[contains(text(),'Max Healthcare Inst.')]/ancestor::tr/following-sibling::*")
print("following siblings from ancestor node ",len(f_siblings))
# all tr will display
following= driver.find_elements(By.XPATH,"//a[contains(text(),'Max Healthcare Inst.')]/ancestor::tr/following::*")
print("following node from ancestor node: ",len(following))
# # preceding siblings
# p_siblings= driver.find_elements(By.XPATH,"//a[contains(text(),'Max Healthcare Inst.')]/ancestor::tr/preceding-sibling::tr")
# print(len(p_siblings))
#following Traverse all element that comes after the current tag
# f_elements = driver.find_elements(By.XPATH,"//a[contains(text(),'Max Healthcare Inst.')]/following::td")
# print(len(f_elements))
# #preceding
# p_elements = driver.find_elements(By.XPATH,"//a[contains(text(),'Max Healthcare Inst.')]/preceding::td")
# print(len(f_elements))
# f_rows = driver.find_elements(By.XPATH,"//a[contains(text(),'Max Healthcare Inst.')]/following::tr")
# print(len(f_rows))
# #preceding
# P_rows = driver.find_elements(By.XPATH,"//a[contains(text(),'Max Healthcare Inst.')]/preceding::tr")
# print(len(P_rows))
# # getting all nodes from table following sipling
# # table_data = driver.find_elements(By.XPATH,"//table[@class='dataTable']/thead/following-sibling::tbody/child::tr")
# # print(len(table_data))
# # for data in table_data:
# #  print(data.text)
# p_sibling = driver.find_elements(By.XPATH,"//a[contains(text(),'Max Healthcare Inst.')]/preceding-sibling::tr")
# print(len(p_sibling))
# f_sibling = driver.find_elements(By.XPATH,"//a[contains(text(),'Max Healthcare Inst.')]/following-sibling::tr")
# print(len(f_sibling))
#descendant (child,grand child elements will get)
descendant_node = driver.find_elements(By.XPATH,"//a[contains(text(),'Max Healthcare Inst.')]/ancestor::tr/descendant::*")
print("no of descendant elements ",len(descendant_node))