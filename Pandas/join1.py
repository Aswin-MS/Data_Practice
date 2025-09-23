import numpy as np
import pandas as pd
lst=[[101,'aswin','ms',22,'kochi'],
      [102,'rajeev','k',21,'calicut'],
      [103,'madhav','s',25,'kochi'],
      [104,'akshay','kk',22,'tvm'],
      [105,'rahul','m',30,'thrissur']]
lst1=[['bigdata',101,25000,'TCS'],
      ['python',102,30000,'Wipro'],
      ['testing',104,32000,'Infosys'],
      ['flutter',103,25000,'TCS'],
      ['python',107,30000,'Cognizant']]
df1=pd.DataFrame(lst)
df1.columns=['id','fname','lname','age','loc']
df2=pd.DataFrame(lst1)
df2.columns=['prof','id','salary','company']
print(df1)
print(df2)
df3=pd.merge(df1,df2,on='id',how="inner")
print(df3)
df4=pd.merge(df1,df2,on='id',how='inner') \
    .loc[df2['prof']=='bigdata'] \
    [['fname','lname','age','prof']]
print(df4)
print('*'*100)
df4=pd.merge(df1,df2,on='id',how='inner'). \
    sort_values(by='age',ascending=False) \
    [['fname','lname','age','prof','salary']] \
    .head(1)
print(df4)
print('*'*100)
df5=pd.merge(df1,df2,on='id',how='inner') \
    .groupby('prof') ['prof'].count() \
    .sort_values(ascending=False)
print(df5)