import numpy as np

M = np.eye(5,5, dtype=int)
M[3:5,0:2] = 2
M[0:3,3:5] = 3
print(M)