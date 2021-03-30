'''
Created on 29-Jul-2019

@author: Amitava
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)
driver.close()