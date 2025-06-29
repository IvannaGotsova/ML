import numpy as np

arrayExample = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

for x in arrayExample:
  print(x)

arrayExample = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])


for x in arrayExample:
  print(x)


for x in arrayExample:
  for y in x:
    for z in y:
        print(z)



for x in np.nditer(arrayExample):
  print(x)


arrayOne = [1, 2, 3, 4, 5]
arrayTwo = [6, 7, 8, 9, 10]

arrayConcatenate = np.concatenate((arrayTwo, arrayOne))
print(arrayConcatenate)

arrayConcatenate = np.stack((arrayOne, arrayTwo), axis=1)
print(arrayConcatenate)

arrayConcatenate = np.vstack((arrayOne, arrayTwo))
print(arrayConcatenate)

arrayConcatenate = np.dstack((arrayOne, arrayTwo))
print(arrayConcatenate)

arrayConcatenate = np.hstack((arrayOne, arrayTwo))
print(arrayConcatenate)

arraySplit = np.array_split(arrayConcatenate, 5)
print(arraySplit[0])
print(arraySplit[1])
print(arraySplit[2])
print(arraySplit[3])
print(arraySplit[4])

arrayExample = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])

arraySplit = np.array_split(arrayExample, 3, axis=2)

print(arraySplit)

arrayExample = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])

elementSearch = np.where(arrayExample == 3)
print(elementSearch)