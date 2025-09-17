import numpy as np
import pandas as pd
df=pd.read_csv("D:/Aswin/Data Science/Daily-Code-Practice/EDA_data_files/missing_data.csv")
print(df)
print(f'shape:{df.shape}')
print('Data types:')
print(df.dtypes)
print('total no. of missing values:')
print(df.isna().sum())
df1=df.fillna(241002)
print(df1.isna().sum())
x=df.iloc[:,:-1]
print(x)
y=df.iloc[:,-1]
print(y)