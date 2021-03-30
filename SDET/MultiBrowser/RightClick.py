'''
Created on 04-Aug-2019

@author: Amitava
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
ele=driver.find_element(By.XPATH, "(//*[contains(text(),'right click me')])[1]")

action=ActionChains(driver)
action.context_click(ele).perform()