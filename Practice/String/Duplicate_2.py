'''
Created on 29-Oct-2019

@author: Amitava
'''
string="good looked"
for i in range(0,len(string)):
    count=1
    for j in range(i+1,len(string)):
        if(string[i]==string[j] and string[i]!=''):
            count+=1
            string=string[:j]+' '+string[j+1:]
            if(count>1 and string[i]!=''):
                print(string[i])

