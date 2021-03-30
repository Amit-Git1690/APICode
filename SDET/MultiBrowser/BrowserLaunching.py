'''
Created on 28-Jul-2019

@author: Amitava
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.get("http://newtours.demoaut.com/")

print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.close()
