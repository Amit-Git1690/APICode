'''
Created on 13-Jul-2019
 
@author: Amitava
'''
   
from selenium import webdriver

chrome_path = r"E:\SeleniumStandard\chromedriver_win32\chromedriver.exe"
baseURL = "https://letskodeit.teachable.com/"

driver = webdriver.Chrome(chrome_path)
driver.maximize_window()
driver.implicitly_wait(3)
driver.get(baseURL)
