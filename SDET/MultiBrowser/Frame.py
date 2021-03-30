'''
Created on 03-Aug-2019

@author: Amitava
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.get("http://seleniumhq.github.io/selenium/docs/api/java/index.html")

driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(4)
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("WebDriver").click()
time.sleep(4)
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("//*[contains(text(),'Deprecated')]").click()
print("Tested Successfully")