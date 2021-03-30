'''
Created on 01-Aug-2019

@author: Amitava
'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get("https://www.expedia.com/")
driver.find_element(By.ID, "tab-flight-tab-hp").click()

driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")
time.sleep(3)
driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYC")

driver.find_element(By.ID,"flight-departing-hp-flight").clear()
driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("10/8/2019")

driver.find_element(By.ID,"flight-returning-hp-flight").clear()
driver.find_element(By.ID,"flight-returning-hp-flight").send_keys("10/12/2019")

driver.find_element(By.XPATH,"(//button[@type='submit'])[11]").click()

wait=WebDriverWait(driver,10)
ele=wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='stopFilter_stops-0']")))
ele.click()
time.sleep(5)
driver.close()
