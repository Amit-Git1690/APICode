'''
Created on 21-Oct-2019

@author: Amitava
'''
m=5
n=5
ch=ord('A')

for i in range(1,m+1):
    for j in range(1,n+1):
        print(chr(ch), end=" ")
        ch+=1;
    print()
        