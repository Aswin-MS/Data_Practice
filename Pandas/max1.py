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