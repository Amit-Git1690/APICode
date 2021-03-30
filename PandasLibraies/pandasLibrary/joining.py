'''
Created on 27-Apr-2020

@author: Amitava
'''
import pandas as pd


df1 = pd.DataFrame({"Int_Rate": [2,1,2,3],"IND_GDR":[50,45,45,67]}, index=[2001,2002,2003,2004])

df2 = pd.DataFrame({"Low_Tier_HPI": [50,40,67,34],"UnEmployement": [1,3,5,6],},index=[2001,2002,2003,2004])

joined = df1.join(df2)
print(joined)