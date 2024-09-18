import time

import XLUtilities
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.cit.com/cit-bank/resources/calculators/certificate-of-deposit-calculator")
driver.implicitly_wait(20)
file = "/Users/ssaguturu/Downloads/Solution/caldata2.xlsx"
rows = XLUtilities.get_row_count(file,"sheet1")
cols = XLUtilities.get_col_count(file,"sheet1")

for r in range(2,rows+1):
    #for c in range(1,cols+1):

    #captured one  row data from xlsx
    principle_amount = XLUtilities.read_data(file,"sheet1",r,1)
    print(principle_amount)
    rate_of_interest = XLUtilities.read_data(file,"sheet1",r,2)
    print(rate_of_interest)
    Length_months = XLUtilities.read_data(file,"sheet1",r,3)
    print(Length_months)
    print()
    compounded_type = XLUtilities.read_data(file,"sheet1",r,4)
    total = XLUtilities.read_data(file,"sheet1",r,5)
    exp_mvalue = XLUtilities.read_data(file,"sheet1",r,6)


    # # passing data to the application
    # # initial deposit amount
    # driver.find_element(By.ID, "mat-input-0").clear()  # clear the field first
    # driver.find_element(By.ID, "mat-input-0").send_keys(principle_amount)  # entering the value
    #
    # #lengthof  cd - months
    # driver.find_element(By.ID, "mat-input-1").clear()
    # driver.find_element(By.ID, "mat-input-1").send_keys(Length_months)
    # # interest rate
    # driver.find_element(By.XPATH, "//input[@id='mat-input-2']").clear()
    # driver.find_element(By.XPATH, "//input[@id='mat-input-2']").send_keys(rate_of_interest)
    #driver.find_element(By.XPATH, "//div[@class='mat-select-arrow-wrapper ng-tns-c109-4']").click()
    #get all mat options
    m_options = driver.find_elements(By.XPATH, "//span[@class='mat-option-text']")
    print(len(m_options))
    for option in m_options:
        print(option.text)
        if option.text == compounded_type:
            option.click()
    selected_value = driver.find_element(By.XPATH, "//mat-select[@id='mat-select-0']")
    print("selected value: ", selected_value.text)
    # # click on lets run the numbers
    # driver.find_element(By.XPATH, "//button[@id='CIT-chart-submit']").click()
    #
    # # Validation comparing expected vs actual value
    # actual_cd = driver.find_element(By.XPATH, "//span[@id='displayTotalValue']").text
    #
    # if total== actual_cd:
    #     print("pass")
    # else:
    #     print("fail")







