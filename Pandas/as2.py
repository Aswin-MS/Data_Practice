import numpy as np
import pandas as pd
t=pd.read_csv("D:/Aswin/Data Science/Daily-Code-Practice/Luminar_Mysql/txn_windows.csv")
print('*'*100)
#1
print(t.shape[0])
print('*'*100)
#2
t2=t.loc[t['dat'].str.startswith('01')] \
    [['oid','cuid','category','product','state']]
print(t2)
#2A:
print(t2.shape[0])
print('*'*100)
#3
t3=t.loc[t['dat'].str.startswith('07')] \
    [['oid','cuid','category','product','state']]
print(t3)
#3B
print(t3.shape[0])
print('*'*100)
#4
t4=t.groupby('category') ['category'].count() \
    .sort_values(ascending=False)
print(t4)
print('*'*100)
#5
t5=t.loc[t['category']=='Outdoor Recreation']
print(t5)
print('*'*100)
#6
t6=t.groupby('method') ['method'].count()
print(t6)
print('*'*100)
#7
t['dat'] = pd.to_datetime(t['dat'], format='%m-%d-%Y')
t7 = t.loc[(t['dat'].dt.month >= 1) & (t['dat'].dt.month <= 7)]
print(t7.shape[0])
print('*'*100)
#8
t8=t.groupby('category') ['pay_amount'].sum() \
    .sort_values(ascending=False)
print(t8)
print('*'*100)
#9
t9=t.groupby('category') ['pay_amount'].max() \
    .sort_values(ascending=False)
print(t9)
print('*'*100)
#10
t10=t.groupby('category') ['pay_amount'].mean() \
    .sort_values(ascending=False)
print(t10)
print('*'*100)
#11
t11=t.groupby('method') ['pay_amount'].sum()
print(t11)
print('*'*100)
#12
t12=t.loc[t['category']=='Indoor Games'].groupby('category') ['pay_amount'].sum()
print(t12)
print('*'*100)
#13
t13=t.groupby('state') ['state'].count() \
    .sort_values(ascending=False)
print(t13)