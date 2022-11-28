import numpy as np
W = np.array([[1,1,1],[2,2,2]])
W[:,1] = np.array([5,5])
print(W) # 这里用array[5,5]这样的一维数组直接可以把W矩阵的第1列替换(维度符合即可)