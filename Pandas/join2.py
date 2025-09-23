import numpy as np
import pandas as pd
c=pd.read_csv("D:/Aswin/Data Science/Daily-Code-Practice/Luminar_Mysql/custom_windows.csv")
o=pd.read_csv("D:/Aswin/Data Science/Daily-Code-Practice/Luminar_Mysql/order_windows.csv")
print(c)
print('*'*100)
print(o)
print('*'*100)
#1
com=pd.merge(c,o,on='id',how='inner')
com1=com [['name','age','location','salary','dat','amount']]
print(com1)
print('*'*100)
#2
com2=com.loc[com['salary']>2500] \
    [['name','age','location','dat','amount']]
print(com2)
print('*'*100)
#3
com3=com.sort_values(by='age',ascending=False) \
    [['name','age','location','salary']] \
    .head(1)
print(com3)
print('*'*100)
#4
com['dat']=pd.to_datetime(com['dat'])
com4=com.sort_values(by='dat',ascending=False) [['name','age','salary','dat','amount']].head(1)
print(com4)