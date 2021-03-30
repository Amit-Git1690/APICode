
'''
Created on 27-Apr-2020

@author: Amitava
'''
import pandas as pd
country = pd.read_csv("F://PythondataRead//Amit.csv", index_col= 0)
country.to_html("F://PythondataRead//edu.html")