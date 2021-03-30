# # '''
# # Created on 06-Nov-2019
# # 
# # @author: Amitava
# # '''
# # # def is_anagram(str1, str2):
# # #     list_str1 = list(str1)
# # #     list_str1.sort()
# # #     list_str2 = list(str2)
# # #     list_str2.sort()
# # # 
# # #     return (list_str1 == list_str2)
# # # 
# # # print(is_anagram('anagram','nagaram'))
# # # print(is_anagram('cat','rat'))
# # 
# # 
# # def anagram(s1, s2):
# #     str1 = ''
# #     str2 = ''
# # 
# #     for i in s1:
# #         str1 += i
# # 
# #     for j in s2:
# #         str2 += j
# # 
# #     if str1 == str2:
# #         return True
# # 
# #     return False
# # # 
# # # print(anagram("cat", "rat"))
# # # print(anagram("Mary", "arMy"))
# # print(anagram("MARY", "ARMY"))
# 
# 
# 
# fstr=input("enter first string:")
# sstr=input("enter second string:")
# 
# if(fstr!=sstr[::-1]):
#     print("it's anagram")
# else:
#     print("Not")


a=input("Enter string 1:")

b=input("Enter string 2:")

count=0

for i in a:

    for j in b:

        if i==j:

            count=count+1

if count==len(a):
    print("Strings are anagram of each other.")

else:
    print("Strings are not anagram of each other.")