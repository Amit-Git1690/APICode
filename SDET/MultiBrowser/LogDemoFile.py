'''
Created on 26-Aug-2019

@author: Amitava
'''
import logging
from builtins import format

logging.basicConfig(filename="C://Users//Amitava//eclipse-workspace//SDET//test.log", format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/ %d/ %y %I: %M: %S %p',level=logging.DEBUG)

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")