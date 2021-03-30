'''
Created on 29-Oct-2019

@author: Amitava
'''
from enum import unique
string="apple my work"
res=" "
for x in string:
    if not (x in res):
        res=res +  x
print(res)