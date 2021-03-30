'''
Created on 04-Aug-2019

@author: Amitava
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.get("https://testautomationpractice.blogspot.com/")

ele=driver.find_element(By.XPATH, "//*[contains(text(),'Copy Text')]")
action=ActionChains(driver)

action.double_click(ele).perform()