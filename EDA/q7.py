import numpy as np
a=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(a)
# print(a.ndim)
# print(a.shape)
# print(a.size)
for i in a:
    for j in i:
        for k in j:
            print(k)