import numpy as np

arrayExample = np.array(1)

print(arrayExample)

arrayExample = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arrayExample)

arrayExample = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])

print(arrayExample)
print(arrayExample.ndim)

arrayExample = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])

print(arrayExample)
print(arrayExample.ndim)
print(arrayExample[1, 1, 1])
print(arrayExample[1, 1, -1])

arrayExample = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

print(arrayExample[0:5])
print(arrayExample[:5])
print(arrayExample[5:])
print(arrayExample[::2])


