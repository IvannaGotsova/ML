import pandas as pd

datasetExample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

seriesExample = pd.Series(datasetExample)

print(seriesExample)

print(seriesExample[0])

seriesExample = pd.Series(datasetExample, index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(seriesExample[1])
print(seriesExample)