from operator import index

import numpy as np
import pandas as pd
a=pd.Series([1,4,7,8,5,2,0])
b=pd.Series([3,6,9,0,2,5,8])
#Arithmetic Operation
# c=a.add(b)
# print(c)
# d=a.sub(b)
# print(d)
# e=a.div(b)
# print(e)
g=a._append(b)
print(g)
h=a._append(b,ignore_index=True)
print(h)
