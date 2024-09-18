import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# def edge_setup():
#
#     driver = webdriver.Edge()
#     return driver
def firefox_setup():

    driver = webdriver.Firefox()
    return driver
def chrome_setup():

    driver = webdriver.Chrome()
    return driver
#my_driver = edge_setup()
#my_driver = firefox_setup()
my_driver = chrome_setup()
my_driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
my_driver.maximize_window()
time.sleep(10)
my_driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()

