# PANDAS ASSIGNMENT 1
################################################################################################################
import numpy as np
import pandas as pd
c=pd.read_csv('D:/Aswin/Data Science/Daily-Code-Practice/customer1.txt',sep=',',header=None)
c.columns=['id','fname','lname','age','prof','loc']
print(c.isna().sum())
c=c.fillna('india')
print(c.isna().sum())
print('*'*100)
#q1:
print(c.shape[0])
print('*'*100)
#q2:
c2=c.drop_duplicates()
#q3:
c3=c2.sort_values(by='age',ascending=False) [['fname','lname','prof','loc']].head(10)
print(c3)
print('*'*100)
#q4:
c4=c2.sort_values(by='age') [['fname','lname','prof','loc']].head(5)
print(c4)
print('*'*100)
#q5:
c5=c2.groupby('loc') ['loc'].count().sort_values(ascending=False)
print(c5)
print('*'*100)
#q6:
c6=c2.loc[c2['loc']=='australia']
print(c6)
print('*'*100)
#q7:
c7=c2.groupby('age') ['age'].count().sort_values(ascending=False)
print(c7)
print('*'*100)
#q8:
c8=c2.groupby('prof') ['prof'].count().sort_values(ascending=False)
print(c8)
print('*'*100)
#q9 A:
c91=c2.loc[c['loc']=='india']
print(c91.shape[0])
print('*'*100)
#q9 B:
c92=c91.groupby('prof') ['prof'].count() \
        .sort_values(ascending=False)
print(c92)
print('*'*100)
#q9 C:
c93=c91.sort_values(by='age',ascending=False) [['fname','lname','age','prof']].head(3)
print(c93)
print('*'*100)
#q9 D:
c94=c91.sort_values(by='age') \
    [['fname','lname','age','prof']] \
    .head(3)
print(c94)
print('*'*100)
#q9 E:
c95=c91.loc[c['age']>40]
print(c95)
print('*'*100)
#q9 F:
c96=c91.loc[(c['age']>=30)&(c['age']<=40)].groupby('prof') ['prof'].count()
print(c96)
print('*'*100)
#q10 A:
c10=c2.loc[c2['loc']=='us']
print(c10.shape[0])
print('*'*100)
#q10 B:
c11=c10.groupby('age') ['age'].count()
print(c11)
#q10 C:
c12=c10.groupby('prof') ['prof'].count().sort_values(ascending=False)
print(c12)
print('*'*100)
#q10 D:
c13=c10.loc[(c10['prof']=='Civil engineer')&(c10['age']>30)]
print(c13)