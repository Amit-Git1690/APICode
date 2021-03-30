'''
Created on 21-Oct-2019

@author: Amitava
'''
from builtins import chr
m=5
n=5


for i in range(1,m+1):
    ch=ord('A')
    for j in range(1,n+1):
        if i>=j:
            print(chr(ch), end=" ")
            ch+=1
        else:
            print(" ", end=" ")
            
    print()
        