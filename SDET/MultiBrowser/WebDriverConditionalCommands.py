'''
Created on 29-Jul-2019

@author: Amitava
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.get("http://newtours.demoaut.com/")
print(driver.title)


user_ele= driver.find_element_by_name("userName")
print(user_ele.is_displayed())      #Return True or False
print(user_ele.is_enabled())        #Return True or False

pwd_ele= driver.find_element_by_name("password")
print(pwd_ele.is_displayed())      #Return True or False
print(pwd_ele.is_enabled())        #Return True or False

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")
driver.find_element_by_name("login").click()

roundtrip=driver.find_element_by_css_selector("input[value=roundtrip]")
print("Status of RoundTrip Button: " , roundtrip.is_selected())

onway=driver.find_element_by_css_selector("input[value=oneway]")
print("Status of onway Button: " , onway.is_selected())
