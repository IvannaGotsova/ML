import numpy as np

arrayOneExample = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3])
arrayTwoExample = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3])

uniqueElementsExample = np.unique(arrayOneExample)
print(uniqueElementsExample)

unionElementsExample = np.union1d(arrayOneExample, arrayTwoExample)
print(unionElementsExample)

intersectionElementsExample = np.intersect1d(arrayOneExample, arrayTwoExample, assume_unique=False)
print(intersectionElementsExample)

setDifferenceElementsExample = np.setdiff1d(arrayOneExample, arrayTwoExample, assume_unique=False)
print(setDifferenceElementsExample)

symetricDifferenceElementsExample = np.setxor1d(arrayOneExample, arrayTwoExample, assume_unique=False)
print(symetricDifferenceElementsExample)