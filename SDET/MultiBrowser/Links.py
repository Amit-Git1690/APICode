'''
Created on 03-Aug-2019

@author: Amitava
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.get("http://newtours.demoaut.com/")
links=driver.find_elements(By.TAG_NAME, "a")
print("Number of Links present in page: " ,len(links))

for link in links:
    print(link.text)
    
# driver.find_element_by_link_text("REGISTER").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "REG").click()