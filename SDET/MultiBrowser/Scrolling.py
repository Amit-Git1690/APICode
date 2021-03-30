'''
Created on 04-Aug-2019

@author: Amitava
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# driver.execute_script("window.scrollBy(0,2000)","")

# ele=driver.find_element(By.XPATH, "(//*[contains(text(),'India')])[2]")
# driver.execute_script("arguments[0].scrollIntoView();" ,ele)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")