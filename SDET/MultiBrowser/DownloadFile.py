'''
Created on 04-Aug-2019

@author: Amitava
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chromeOptions=Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory": "E:/"})
 

driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe',chrome_options=chromeOptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.find_element(By.XPATH, "//textarea[@id='textbox']").send_keys("Amitava")
driver.find_element(By.XPATH,"//button[@id='createTxt']").click()
driver.find_element(By.XPATH,"//a[@id='link-to-download']").click()
