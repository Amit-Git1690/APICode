'''
Created on 28-Aug-2019

@author: Amitava
'''
import unittest
from selenium  import webdriver

class SearchEnginesTest(unittest.TestCase):
    def test_google(self):
        driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
        driver.get("https://www.google.com/")
        print("Title of the Page: " +self.driver.title)
        self.driver.close()

    def test_bing(self):
        driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
        driver.get("https://bing.com/")
        print("Tite of the page:" + self.driver.title)
        self.driver.close()
        
if __name__=="__main__":
    unittest.main()

