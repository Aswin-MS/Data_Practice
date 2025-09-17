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
# df1=a.loc[a['age']>22]
# print(df1)
# print('*'*100)
# df2=a.loc[a['loc']=='Chennai'] [['fname','lname','age']]
# print(df2)

#17sept
# df3=a.loc[(a['age']>22)&(a['loc']=='Chennai')]
# print(df3)

#sort():
# dfs=a.sort_values(by='age')
# print(dfs)

#q1
q1=a.loc[a['age']>23] [['fname','lname','age']]
print(q1)
print('*'*100)
#q2
q2=a.loc[a['age']<22] [['fname','lname']]
print(q2)
#q3
print('*'*100)
q3=a.sort_values(by='age',ascending=False) [['fname','lname','age','phn']].head(1)
print(q3)
#q4
print('*'*100)
q4=a.sort_values(by='age') [['fname','lname','age']].head(1)
print(q4)
#q5
print('*'*100)
q5=a.loc[a['loc']=='Chennai'].sort_values(by='age',ascending=False) [['fname','lname','age']].head(1)
print(q5)