import numpy as np
import pandas as pd
df=pd.read_csv("D:\Aswin\Data Science\Daily-Code-Practice\Luminar_Mysql\missing_data.csv")
print(df)
print(df.isna().sum())
# df1=df.fillna(285)
# print(df1)
# df.fillna(295,inplace=True)
# print(df)
# df['Calories'].fillna(680,inplace=True)
# print(df)
# df['Date'].fillna('2025/12/25',inplace=True)
# df.fillna({'Date':'123'},inplace=True)
# print(df['Calories'].unique())
# m=df['Calories'].mean()
# print(m)
# df['Calories'].fillna(m,inplace=True)
# print(df)
# print('*'*100)
# d=df['Date'].mode()[0]
# print(d)
# df['Date'].fillna(d,inplace=True)
# print(df)

#------------------>
#25 SEPT
#------------------>

# df.dropna(inplace=True,ignore_index=True)
# df.dropna(subset=['Date'],inplace=True,ignore_index=True)
# df.dropna(subset=['Calories'],inplace=True,ignore_index=True)
# print(df)
x=df['Duration'].mode()[0]
print(x)
df.loc[7,'Duration']=x
print(df)
print('*'*100)
#assume calories above 400 is wrong data
#use mean to fill that data
c=df['Calories'].mean()
print(c)
df.loc[df['Calories']>400,'Calories']=c
print(df)
for i in df:
    print(i)