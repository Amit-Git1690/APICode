'''
Created on 03-Aug-2019

@author: Amitava
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH, "//button[contains(text(),'Click Me')]").click()
time.sleep(4)
# driver.switch_to_alert().accept()
driver.switch_to_alert().dismiss()