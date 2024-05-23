import np
import numpy as np

def addFunctionExample(x, y, z, a):
  return x + y + z + a

addNumpyAddFunctionExample = np.frompyfunc(addFunctionExample, 4, 1)

print(addNumpyAddFunctionExample([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]))

