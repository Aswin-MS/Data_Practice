import numpy as np
import pandas as pd
c=pd.read_csv('D:/Aswin/Data Science/Daily-Code-Practice/customer1.txt',sep=',',header=None)
c.columns=['id','fname','lname','age','prof','loc']
c1=c.groupby('prof') ['age'].max()
print(c1.sort_values(ascending=False))
print('*'*100)
c2=c.groupby('loc') ['age'].max() \
    .sort_values(ascending=False)
print(c2)
print('*'*100)
print(c['age'].max())
print('*'*100)
#22 SEPT
#Min()
min=c.groupby('prof') ['age'].min() \
    .sort_values(ascending=False)
print(min)
print('*'*100)
print(c['age'].min())
print('*'*100)
minl=c.groupby('loc') ['age'].min() \
    .sort_values()
print(minl)
print('*'*100)
#Sum():
summ=c.groupby('prof') ['age'].sum() \
    .sort_values(ascending=False)
print(summ)
print(c['age'].sum())
print('*'*100)
#Mean():
av=c.groupby('prof') ['age'].mean() \
    .sort_values(ascending=False)
print(av)
print(c['age'].mean())