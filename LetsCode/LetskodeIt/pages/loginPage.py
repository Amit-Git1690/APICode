from base.selenium_driver import SeleniumDriver
import logging
import utilities.custom_Logger as cl

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
    
    def verifyLoginSuccessful(self):
        result= self.isElementPresent(".//*[@id='navbar']//span[text()='Test User']", locatorType="xpath")
        return result
        
        
    def varifyLoginFail(self):
        result=self.isElementPresent("//div[contains(text(),'Invalid email or password.')]", locatorType="xpath")
        return result
    
    def clearFields(self):
        emailField=self.getElement(locator=self._email_field)
        emailField.clear()
        passwordFiels=self.getElement(locator=self._password_field)
        passwordFiels.clear()
        
    def verifyTitle(self):
        if "Google" in self.getTitle():
            return True
        else:
            return False
        
        