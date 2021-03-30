'''
Created on 03-Aug-2019

@author: Amitava
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.get("file:///E:/SeleniumStandard/sample.html")
rows=len(driver.find_elements(By.XPATH,"/html/body/table/tbody/tr"))
print(rows)
cols=len(driver.find_elements(By.XPATH,"/html/body/table/tbody/tr/th"))
print(cols)

print("Firstname"+"    "+"Lastname"+"    "+"Age")

for r in range(2,rows+1):
    for c in range(1,cols+1):
        value=driver.find_element(By.XPATH, "/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end="        ")
    print()
