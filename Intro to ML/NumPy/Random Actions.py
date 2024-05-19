import numpy as np
from numpy import random

arrayExample = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

random.shuffle(arrayExample)

print(arrayExample)

arrayPermutation = random.permutation(arrayExample)

print(arrayPermutation)
print(arrayExample)

