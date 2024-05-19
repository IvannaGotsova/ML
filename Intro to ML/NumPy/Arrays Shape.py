import numpy as np

arrayExample = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])

print(arrayExample.ndim)
print(arrayExample.shape)

arrayExample = arrayExample.reshape(1, 20)

print(arrayExample)
print(arrayExample.size)

arrayExample = arrayExample.reshape(4, 5)

print(arrayExample)
print(arrayExample.size)

arrayExample = arrayExample.reshape(2, 2, 5)

print(arrayExample)
print(arrayExample.size)