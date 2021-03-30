'''
Created on 16 Jul 2019

@author: 612495164
'''

import pytest
from selenium import webdriver
from base.webDriverFactory import WebDriverFactory
from selenium.webdriver import chrome
from base import webDriverFactory


@pytest.yield_fixture()
def setUp():
    print("Running method level setting")
    yield
    print("Running method level tearDown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setting")
    
    wdf=WebDriverFactory(browser)
    driver=wdf.getWebDriverInstance()
    
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")
 
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")