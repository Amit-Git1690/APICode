'''
Created on 20-Oct-2019

@author: Amitava
'''
m=5
n=5
for i in range(1,m+1):
    for j in range(1,n+1):
        if i==j:
            print( "*", end=" ")
        elif j<i:
            print("#", end=" ")
        else:
            print(i , end=" ")
    print()
    