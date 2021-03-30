'''
Created on 29-Oct-2019

@author: Amitava
'''
string1="i am reading"
string2="i am writing"
res=" "
for i in string1:
    if not (i in string2):
        res+=" "
print(res)
        