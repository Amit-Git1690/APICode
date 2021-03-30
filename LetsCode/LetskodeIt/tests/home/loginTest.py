'''
 Created on 11 Jul 2019
 @author: 612495164
 '''

        
from pages.loginPage import LoginPage 
import unittest
import pytest
from utilities.test_status import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp", "setUp" )
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lp = LoginPage(self.driver)
        self.ts=TestStatus(self.driver)
        


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1= self.lp.verifyTitle()
        self.ts.mark(result1, "Title is verified")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test valid Login", result2, "Login was successful")
       

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.varifyLoginFail()
        assert result == True
