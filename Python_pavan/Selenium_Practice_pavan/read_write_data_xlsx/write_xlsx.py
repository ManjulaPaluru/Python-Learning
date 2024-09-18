import openpyxl
from selenium import webdriver

driver =  webdriver.Chrome()
file = "/Users/ssaguturu/Downloads/country_test.xlsx"
workbook = openpyxl.load_workbook(file)
sheet = workbook.active

for r in range(1,5): # give how many rows to wnat to add data
    for c in range(1,5): # give how many columns to
        sheet.cell(r,c).value = "welcome"
workbook.save()
