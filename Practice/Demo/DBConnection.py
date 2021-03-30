'''
Created on 26-Oct-2019

@author: Amitava
'''
import cx_Oracle
import os 
os.environ['PATH']='E:\\Software\\instantclient-basic-windows.x64-19.3.0.0.0dbru.zip\\instantclient_19_3'
# Establish connection to the database

cx_Oracle.connect() 