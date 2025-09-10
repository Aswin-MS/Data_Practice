import numpy as np
a=np.array([[1,2,3,4],[4,3,5,6],[5,1,2,1],[1,6,8,9]])
print(a)
print('')
#3D (2,8):
# b=a.reshape(1,2,8)
# print(b)
#1D:
c=a.reshape(16)
print(c)