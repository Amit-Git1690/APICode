'''
Created on 26-Oct-2019

@author: Amitava
'''
from builtins import int
a={ }
n=int(input("Enter the Number of Element: "))
for i in range(n):
    key=input("Enter Key:")
    val=input("Enter Value:")
    a[key]=val
    
    print(a)
    print("-----------------")
    