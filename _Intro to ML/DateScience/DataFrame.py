import pandas as pd

data = {'columnOne': [1, 1, 6, 8, 2, 9, 8, 3, 4, 7], 'columnTwo': [4, 2, 4, 3, 5, 6, 9, 5, 7, 1], 'columnThree': [7, 8, 5, 7, 1, 1, 2, 6, 9, 1]}

dataframe = pd.DataFrame(data=data)

print(dataframe)

row_count = dataframe.shape[0]
print(row_count)

column_count = dataframe.shape[1]
print(column_count)