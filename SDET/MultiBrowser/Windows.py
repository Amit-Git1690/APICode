'''
Created on 03-Aug-2019

@author: Amitava
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element(By.XPATH,"(//button[contains(text(),'click')])[1]").click()
current_window=driver.current_window_handle
print(current_window)
currnt_title=driver.title

handles=driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    title_window=driver.title
    print(title_window)
    if title_window in currnt_title:
        driver.close()
    
driver.quit()
