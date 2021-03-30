'''
Created on 04-Aug-2019

@author: Amitava
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.get("http://testautomationpractice.blogspot.com/")
driver.switch_to.frame("frame-one1434677811")
driver.find_element(By.XPATH,"//input[@id='RESULT_FileUpload-11']").send_keys("E://Rose.jpg")