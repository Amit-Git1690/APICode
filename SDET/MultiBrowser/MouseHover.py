'''
Created on 04-Aug-2019

@author: Amitava
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.get("https://opensource-demo.orangehrmlive.com")

driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()

admin=driver.find_element(By.XPATH,"(//*[contains(text(),'Admin')])[2]")
user_management=driver.find_element(By.XPATH, "(//*[contains(text(),'User Management')])")
users=driver.find_element(By.XPATH, "(//*[contains(text(),'Users')])[1]")

action=ActionChains(driver)
action.move_to_element(admin).move_to_element(user_management).move_to_element(users).click().perform()
