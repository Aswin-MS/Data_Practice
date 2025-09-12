#JOIN
import numpy as np
#1D
# a=np.array([1,2,4,5,3,8,7,4,5])
# b=np.array([4,8,9,3,2,4,1,5,4])
# c=np.concatenate([a,b])
# print(c)
#2D:
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[2,3,4],[6,5,4],[5,7,1]])
c=np.concatenate([a,b],axis=1)
print(c)
