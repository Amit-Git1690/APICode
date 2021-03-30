'''
Created on 25-Aug-2019

@author: Amitava
'''

from selenium import webdriver
from MultiBrowser import ExcelUtils

driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.get("http://newtours.demoaut.com/")
print(driver.title)


path="E:\LoginTest.xlsx"
rows=ExcelUtils.getRowCount(path,"Sheet1")

for r in range(2,rows+1):
    uname=ExcelUtils.readData(path,"Sheet1",r,1)
    pword=ExcelUtils.readData(path, "Sheet1", r, 2)
    
    driver.find_element_by_name("userName").send_keys(uname)
    driver.find_element_by_name("password").send_keys(pword)
    driver.find_element_by_name("login").click()
     
    if driver.title=="Find a Flight: Mercury Tours:":
        print("test is passed")
        ExcelUtils.writeData(path,"Sheet1",r,3,"test passed")
    else:
        print("test is  failed")
        ExcelUtils.writeData(path,"Sheet1",r,3,"test failed")
    driver.find_element_by_link_text("Home").click()
        
       

