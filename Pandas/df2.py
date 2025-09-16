#nested dictionary
import numpy as np
import pandas as pd
d={'id':[101,102,103,104,105],
   'fname':['aswin','anil','amrita','arjun','anu'],
   'lname':['ms','tp','s','r','k'],
   'age':[21,22,25,20,25],
   'prof':['python','bigdata','testing','webdev','flutter'],
   'salary':[20000,21000,19000,15000,30000],
   'location':['kochi','calicut','tvm','calicut','trissur']}
df=pd.DataFrame(d)
print(df)