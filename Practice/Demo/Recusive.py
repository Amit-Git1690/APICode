'''
Created on 26-Oct-2019

@author: Amitava
'''
def disp(n):
    if n<=0:
        print(n, end=" ")
        return
    print(n ,end=" ")
    disp(n-1)
    
a=disp(10)
print(a)