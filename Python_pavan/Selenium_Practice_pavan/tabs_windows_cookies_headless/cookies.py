from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com")
cookies = driver.get_cookies()
print(len(cookies))
# print all cookie details
for c in cookies:
    print(c)
# printing specific details of cookie, cookie have so many attributes like name value, expire date
    #print(cookie.get("name"))
    #print(c.values())
    #print(c.keys())
    #print(c.get("name"),":" ,c.get("value"))
# Add cookie to the browser
driver.add_cookie({"name" : "My cookie", "value" :"1234"})
c_count_after_adding_cookie = driver.get_cookies()
print(len(c_count_after_adding_cookie))
# Delete specific cookie from the browser
driver.delete_cookie("My cookie")
c_count_after_delete_cookie = driver.get_cookies()
print(len(c_count_after_delete_cookie))
driver.delete_all_cookies()
c_deleted_all_cookies = driver.get_cookies()
print(len(c_deleted_all_cookies))


