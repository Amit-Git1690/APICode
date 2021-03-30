'''
Created on 01-Aug-2019

@author: Amitava
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from MultiBrowser.BrowserLaunching import driver

driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")


status=driver.find_element(By.XPATH,"//input[@value='Radio-0' and  @type='radio']/..").is_displayed()    
print("Status is Displayed or Not: " + (str(status)))
status=driver.find_element(By.XPATH,"//input[@value='Radio-0' and  @type='radio']/..").is_selected()
print("Status is Selected: " +(str(status)))

male=driver.find_element(By.XPATH,"//input[@value='Radio-0' and  @type='radio']/..")
male.click()

status_res=driver.find_element(By.XPATH,"//input[@value='Radio-0' and  @type='radio']/..").is_selected()
print("Status is Selected: " +(str(status_res)))

driver.find_element_by_xpath("//input[@id='RESULT_CheckBox-8_4' and  @type='checkbox']/..").click()
driver.find_element_by_xpath("//input[@id='RESULT_CheckBox-8_3' and  @type='checkbox']/..").click()