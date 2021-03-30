'''
Created on 28-Oct-2019

@author: Amitava
'''
n=5
factorial=1
if(n<0):
    print("Sorry factorial does not exists for negative number")
elif n==0 & n==1:
    print("The Factorial of 0 is 1")
else:
    for i in range(1,n+1):
        factorial=factorial*i
    print("The factorial of", n ,"is", factorial)