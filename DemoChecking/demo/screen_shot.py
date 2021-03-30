'''
Created on 20-Jul-2019

@author: Amitava
'''
# from selenium import webdriver
# 
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
# options.binary_location = "/DemoChecking/screenshotFolder"
# driver = webdriver.Chrome(executable_path=r"E:\SeleniumStandard\chromedriver_win32\chromedriver.exe")
# 
# driver.get('https://python.org')
# driver.save_screenshot("/DemoChecking/screenshotFolder/screenshot.png")
# 
# driver.close()




import selenium.webdriver as webdriver
import contextlib

@contextlib.contextmanager
def quitting(thing):
    yield thing
    thing.quit()

with quitting(webdriver.Firefox()) as driver:
    driver.implicitly_wait(10)
    driver.get('http://www.google.com')
    driver.get_screenshot_as_file('/tmp/google.png') 
    # driver.save_screenshot('/tmp/google.png')