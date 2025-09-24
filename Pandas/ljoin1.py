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
df3=pd.merge(df1,df2,on='id',how='left')
print(df3)
print('*'*100)
df4=pd.merge(df1,df2,on='id',how='right')
print(df4)
print('*'*100)
df5=pd.merge(df1,df2,on='id',how='outer')
print(df5)