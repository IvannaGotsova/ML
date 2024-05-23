import numpy as np

oneExample = 12
twoExample = 24
arrayExample = np.array([2, 4, 7, 1, 23, 45, 77, 67, 34, 51])

lcmExample = np.lcm(oneExample, twoExample)
lcmArrayExample = np.lcm.reduce(arrayExample)

print(lcmExample)
print(lcmArrayExample)