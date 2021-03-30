'''
Created on 18-Nov-2019

@author: Amitava
'''

def rev_Pyd(rows):
    for i in range(rows):
        print(" " *(0,rows-i) + " " *(0,i))
    print()


res=rev_Pyd(5)
print(res)