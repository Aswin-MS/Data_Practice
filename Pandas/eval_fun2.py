import numpy as np
import pandas as pd
a=pd.read_csv("D:/Aswin/Data Science/Daily-Code-Practice/sample4.txt",sep=',',header=None)
a.columns=['id','fname','lname','age','phn','loc']
#each loc count desc:
df1=a.groupby('loc') ['loc'].count() \
     .sort_values(ascending=False)
print(df1)
#each age group count asc
df2=a.groupby('age') ['age'].count() \
     .sort_values()
print(df2)