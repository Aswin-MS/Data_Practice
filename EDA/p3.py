import numpy as np
from numpy.lib.format import dtype_to_descr

a=np.array([[1.2,2.5,3.1,4.1],[0.5,4.2,8.2,6.3],[1.5,1.2,1.4,2.4],[8.4,8.7,1.5,6.3]])
print(a)
b=np.floor(a)
print(b)
print()
c=np.ceil(a)
print(c)
print()
d=np.round(a)
print(d)