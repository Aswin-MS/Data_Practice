import numpy as np
import pandas as pd
cs=pd.read_csv('D:/Aswin/Data Science/Daily-Code-Practice/customer1.txt',sep=',',header=None)
cs.columns=['id','fname','lname','age','prof','loc']
#q1:
cs1=cs [['fname','lname','age','prof']]
print(cs1)
print('*'*100)
#q2:
cs2=cs.loc[cs['age']>50] [['fname','lname','age','prof']]
print(cs2)
print('*'*100)
#q3:
cs3=cs.loc[(cs['age']>25) & (cs['age']<40)]
print(cs3)
#q4:
print('*'*100)
cs4=cs.loc[cs['loc']=='india'] [['fname','lname','age','prof']]
print(cs4)
#q5:
print('*'*100)
cs5=cs.sort_values(by='age') [['fname','lname','age']].head(3)
print(cs5)
#q6:
print('*'*100)
cs6=cs.loc[(cs['loc']=='india') & (cs['prof']=='Doctor')].sort_values(by='age',ascending=False) [['fname','lname','age','prof']].head(1)
print(cs6)
#q7:
print('*'*100)
cs7=cs.loc[cs['loc']=='uk'].sort_values(by='age',ascending=False) [['fname','lname','age','prof']].head(10)
print(cs7)
#q8:
print('*'*100)
cs8=cs.loc[(cs['loc']=='us') & (cs['age']>60)] [['fname','lname','age','prof']]
print(cs8)
#q9:
print('*'*100)
cs9=cs.loc[cs['prof']=='Pilot'].sort_values(by='age',ascending=False) [['fname','lname','age']].head(3)
print(cs9)
#q10:
print('*'*100)
cs10=cs.loc[cs['prof']=='Pilot'].sort_values(by='age').head(1)
print(cs10)