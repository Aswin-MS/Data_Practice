import numpy as np
import pandas as pd
a=pd.read_csv("D:/Aswin/Data Science/Daily-Code-Practice/sample4.txt",sep=',',header=None)
a.columns=['id','fname','lname','age','phn','loc']
# print(a)
# df=a[['fname','lname','age']]
# print(df)
# df=a[['fname','lname','age']].head(3)
# print(df)
#
# df1=a[['fname','lname']].tail(1)
# print(df1)

#FILTER
df1=a.loc[a['age']>22]
print(df1)
print('*'*100)
df2=a.loc[a['loc']=='Chennai'] [['fname','lname','age']]
print(df2)