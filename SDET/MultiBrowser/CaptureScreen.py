'''
Created on 04-Aug-2019

@author: Amitava
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

 

driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.get("http://demo.automationtesting.in/FileDownload.html")

# driver.save_screenshot("E:\ScreenShot\homepage.png")

driver.get_screenshot_as_file("E:\ScreenShot\homepageNew.png")
