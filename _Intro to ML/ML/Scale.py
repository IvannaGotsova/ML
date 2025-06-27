import pandas as pd
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

dataset = [
["Ivan", "22", "6", "91.2"],
["Petar", "35", "5", "63.5"],
["Dimitar", "43", "5", "90.23"],
["Stephan", "45", "4", "92.7"],
["Philip", "49", "6", "98.2"],
["Robert", "23", "3", "88.1"],
["Andrei", "34", "4", "95.0"]
]

dataframe = pd.DataFrame(dataset, columns=['Name', 'Age', 'Grade', 'Percentage'])

X = dataframe[['Age', 'Grade']]


scaledX = scale.fit_transform(X)

print(scaledX)