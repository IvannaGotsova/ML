import numpy as np

arrayExample = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arrayExampleCopy = arrayExample.copy()
arrayExampleCopy[0] = 10

print(arrayExampleCopy)
print(arrayExample)

arrayExample = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arrayExampleView = arrayExample.view()
arrayExampleView[0] = 10

print(arrayExampleView)
print(arrayExample)