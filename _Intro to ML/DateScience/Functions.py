import pandas as pd

data = {'columnOne': [1, 1, 6, 8, 2, 9, 8, 3, 4, 7], 'columnTwo': [4, 2, 4, 3, 5, 6, 9, 5, 7, 1], 'columnThree': [7, 8, 5, 7, 1, 1, 2, 6, 9, 1]}

dataframe = pd.DataFrame(data=data)

columnOneMax = dataframe['columnOne'].max()
columnTwoMin = dataframe['columnTwo'].min()
columnThreeMean = dataframe['columnThree'].mean()

print(f"Maximum value in column 'columnOne': {columnOneMax}")
print(f"Minimum value in column 'columnTwo': {columnTwoMin}")
print(f"Mean value in column 'columnThree': {columnThreeMean}")




