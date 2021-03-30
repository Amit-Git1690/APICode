'''
Created on 26-Aug-2019

@author: Amitava
'''
'''
Created on 26-Aug-2019

@author: Amitava
'''
import logging
from builtins import format

logging.basicConfig(filename="C://Users//Amitava//eclipse-workspace//SDET//test.log", format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/ %d/ %y %I: %M: %S %p')

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")