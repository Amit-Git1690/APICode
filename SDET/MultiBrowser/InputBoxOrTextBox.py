'''
Created on 01-Aug-2019

@author: Amitava
'''
 
from selenium import webdriver
from selenium.webdriver.common.by import By
from MultiBrowser.BrowserLaunching import driver


driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
obj=driver.find_elements(By.CLASS_NAME, 'text_field')
print("Number of Input Boxes:"  + str(len(obj)))

status=driver.find_element(By.ID,"RESULT_TextField-1").is_displayed()    
print("Status is Displayed or Not: " + (str(status)))
status=driver.find_element(By.ID,"RESULT_TextField-2").is_enabled()
print("Status is Enabled: " +(str(status)))

driver.find_element(By.ID, "RESULT_TextField-1").send_keys("Amitava") 
driver.find_element(By.ID,"RESULT_TextField-2").send_keys("Chakraborty")
driver.find_element_by_id("RESULT_TextField-3").send_keys("9775323005")
    