import numpy as np
import pandas as pd
c=pd.read_csv("D:/Aswin/Data Science/Daily-Code-Practice/Luminar_Mysql/customer5_windows.csv")
#1
print(c.shape[0])
print('*'*100)
#2
c2=c.sort_values(by='age',ascending=False) \
    [['fname','lname','age']].head(5)
print(c2)
print('*'*100)
#3
c3=c.groupby('prof') ['prof'].count() \
    .sort_values(ascending=False)
print(c3)
print('*'*100)
#4
c4=c.groupby('prof') ['salary'].sum() \
    .sort_values(ascending=False)
print(c4)
#5
print('*'*100)
c5=c.groupby('loc') ['age'].max() \
    .sort_values(ascending=False)
print(c5)
#6
print('*'*100)
c6=c.groupby('age') ['salary'].mean() \
    .sort_values(ascending=False)
print(c6)
#7:
print('*'*100)
c7=c.groupby('prof') ['age'].max() \
    .sort_values(ascending=False)
print(c7)
#8
print('*'*100)
c8=c.groupby('prof') ['age'].min()
print(c8)
#9
print('*'*100)
c9=c.loc[c['loc']=='india'] \
    .groupby('prof') ['age'].max() \
    .sort_values(ascending=False)
print(c9)