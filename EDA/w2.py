import numpy as np
# a=np.arange(1,51)
# b=a%2==0
# c=a[b].reshape(5,5)
# print(c)
a=np.arange(1,101)
b=a%5==0
c=a[b].reshape(1,2,10)
print(c)