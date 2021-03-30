'''
Created on 27-Apr-2020

@author: Amitava
'''

import pandas as pd


df1 = pd.DataFrame({"HPI": [80,90,70,60],"Int_Rate": [2,1,2,3],"IND_GDR":[50,45,45,67]}, index = [2001,2002,2003,2004])

df2 = pd.DataFrame({"HPI": [80,90,70,60],"Int_Rate": [2,1,2,3],"IND_GDR":[50,45,45,67]}, index = [2005,2006,2007,2008])

# merge = pd.merge(df1, df2)
merge = pd.merge(df1, df2, on="HPI")
print(merge)