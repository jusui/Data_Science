import numpy as np
import scipy as sp

ndarray = np.array([1, 2, 3])
print (ndarray)

ndtuple = np.array((1, 2, 3))
print(ndtuple)

ndnest = np.array([[0, 2, 4], [1, 3, 5]])
print(ndnest)

arraycmp = np.array([ndarray, [2, 4, 0]])
print(arraycmp)

# [0., 0., 0.]Vector (Length 3)
vector_1 = np.zeros(3)
print(vector_1)

# [[1, 1, 1,] , [1, 1, 1,] , [1, 1, 1,] , [1, 1, 1,]]
vector_2 = np.ones((3, 4))
print(vector_2)

vector_3 = np.array([[1,2,3],[4,5,6]])
vector_4 = np.zeros_like(vector_3)
print(vector_4)

# 4 * 4 Unit matrix
id_array = np.identity(4)
print(id_array)
print(id_array.dtype)

id_array = np.identity(4, dtype = complex)
print(id_array)
print(id_array.dtype)



