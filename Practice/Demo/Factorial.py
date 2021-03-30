'''
Created on 26-Oct-2019

@author: Amitava
'''
from _ast import In
def fact(n):
#     n=int(input("Enter the Number:"))
    if n==0 or n==1:
        return 1
#     if n in (0,1):
#         return n
    return n*fact(n-1)

a=fact(5)
print(a)