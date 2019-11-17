# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 03:15:57 2019


"""

import pandas as pd 
import numpy as np

list1=list();
df=pd.read_excel(r'Kitap1.xlsx')
column_name=input ("Hangi Sütun? ")
str(column_name)

df=pd.DataFrame(df,columns=[column_name])
x = df[column_name]
x=np.array(df) #seçilen kolonu diziye aktardık
for q in x:
    if (q=='_+-'):
        continue
    else:
        list1.append(q)
#x dizisinden sayı olmayanları çıkardık
        
   

print("Seçilen Sütunun en son anlamlı karakteri: ",max(list1))
