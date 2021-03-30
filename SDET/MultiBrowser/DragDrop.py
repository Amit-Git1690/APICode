'''
Created on 04-Aug-2019

@author: Amitava
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.get("http://.www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

source_ele=driver.find_element(By.XPATH, "(//*[contains(text(),'Rome')])[2]")
dest_ele=driver.find_element(By.XPATH, "(//*[contains(text(),'Italy')])")

action=ActionChains(driver)
action.drag_and_drop(source_ele,dest_ele).perform()