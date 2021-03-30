'''
Created on 25-Aug-2019

@author: Amitava
'''

from selenium import webdriver

driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.get("https://www.amazon.in/")

# Capture all the cookies created by Browser

cookies=driver.get_cookies()
print(len(cookies)) #print number of cookies have been created
print(cookies)  #print all the cookies pairs

#Adding new cookie to the browser

cookie={'name':'Mycookie','value':'1234566788'}
driver.add_cookie(cookie)

cookies=driver.get_cookies()
print(len(cookies)) #print number of cookies after adding new cookie
print(cookies)  #print all the cookies pairs

#Delete the Cookies

driver.delete_cookie('Mycookie')
cookies=driver.get_cookies()
print(len(cookies)) #print number of cookies after deleting the cookie
print(cookies)  #print all the cookies pairs
