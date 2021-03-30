'''
Created on 18 Jul 2019

@author: 612495164
'''
"""
@package base

WebDriver Factory class implementation ----It creates a web driver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""

import traceback
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://letskodeit.teachable.com/"
#                 Set chrome driver
        if self.browser == "chrome":
              driver = webdriver.Chrome(executable_path=r'C:\SeleniumStandalone\fg.exe');
              driver = webdriver.IeOptions()
            
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=r'C:\SeleniumStandalone\geckodriver.exe');
            driver = webdriver.Firefox()
      
        else:
             driver = webdriver.Chrome(executable_path=r'C:\SeleniumStandalone\chromedriver.exe');
             driver = webdriver.Chrome()
            
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver