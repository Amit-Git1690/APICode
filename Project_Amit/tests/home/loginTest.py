'''
Created on 23-Jul-2019

@author: Amitava
'''

        
from pages.loginPage import LoginPage 
import unittest
import pytest
from utility.test_status import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp","setUp" )
class LoginTests(unittest.TestCase):
        
    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lpage=LoginPage(self.driver)
        self.tpage=TestStatus(self.driver)
        

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lpage.login("test@email.com","abcabc")
        result1= self.lpage.verifyTitle()
        self.tpage.mark(result1, "Title is verified")
        result2 = self.lpage.verifyLoginSuccessful()
        self.tpage.markFinal("test valid Login", result2,"Login was successful")
       

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lpage.login("test@email.com", "abcabcabc")
        result = self.lpage.varifyLoginFail()
        assert result == True
