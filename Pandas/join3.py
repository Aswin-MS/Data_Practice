import numpy as np
import pandas as pd
s=pd.read_csv("D:\Aswin\Data Science\Daily-Code-Practice\Luminar_Mysql\student.csv")
r=pd.read_csv("D:/Aswin/Data Science/Daily-Code-Practice/Luminar_Mysql/result.csv")

res=pd.merge(s,r,on='roll',how='inner') \
    .loc[r['res']=='pass'] [['name','roll','res']]
print(res)