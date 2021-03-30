'''
Created on 03-Aug-2019

@author: Amitava
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path='E:\SeleniumStandard\chromedriver_win32\chromedriver.exe')
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

drop_box=driver.find_element_by_id("RESULT_RadioButton-9")
drop_ele=Select(drop_box)

drop_ele.select_by_visible_text("Morning")

# drop_ele.select_by_index(2)

# drop_ele.select_by_value("Radio-2")

print(len(drop_ele.options))

all_option=drop_ele.options
for option in all_option:
    print(option.text)
