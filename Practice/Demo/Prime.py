# '''
# Created on 28-Oct-2019
# 
# @author: Amitava
# '''
# n=11
# if(n>1):
#     for i in range (int(2,n/2)):
#         if(n%i==0):
#             print(n,"is not a prime number")
#         else:
#             print(n," is a Prime Number")
# else:
#     print(n,"  is not prime")
# 
num = int(input("Enter a number: "))  
   
if num > 1:
    for i in range(2,num):
        if (num % i) == 0: 
            print(num,"is not a prime number") 
#             print(i,"times",num//i,"is",num)
            break  
        else: 
            print(num,"is a prime number")  
          
else: 
    print(num,"is not a prime number") 

#Take the input from the user:  
 
# lower = int(input("Enter lower range: "))  
# upper = int(input("Enter upper range: "))  
#   
# for num in range(lower,upper + 1):  
#     if num > 1:  
#         for i in range(2,num):  
#             if (num % i) == 0:  
#                 break  
#     else:  
#         print(num)  