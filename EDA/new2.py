import numpy as np
a=np.array([[1,2,3,4],[4,3,5,6],[5,1,2,1],[1,6,8,9]])
print(a)
print('')
#3D (2,8):
# b=a.reshape(1,2,8)
# print(b)
#1D:
# c=a.reshape(16)
# print(c)
#
# #sum of a
# d=np.sum(a)
# print(d)
#
# e=np.sum(a,axis=1)
# print(e)
#
# f=np.max(a,axis=0)
# print(f)

# g=np.min(a,axis=1)
# print(g)
print()
# f=np.sort(a)
# print(f)
# f=np.sort(a,axis=0)
# print(f)

h=np.argmax(a)
print(h)