import numpy as np
import pandas as pd
c=pd.read_csv("D:/Aswin/Data Science/Daily-Code-Practice/customer1.txt",sep=',',header=None)
c.columns=['id','fname','lname','age','prof','loc']
df=c[['fname','lname','age','prof']].head(50)
print(df)
print('#'*100)
df1=c[['fname','lname','age']].tail(25)
print(df1)
print('#'*100)
df2=c.iloc[10:25,1:4]
print(df2)
print('*'*100)
x=c.iloc[:,0:5]
print(x)
print('*'*100)
y=c.iloc[:,::-6]
print(y)