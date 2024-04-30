import pandas as pd
from sklearn import linear_model

dataset = [
["Ivan", "1", "11", "11"],
["Petar", "2", "22", "22"],
["Dimitar", "3", "33", "33"],
["Stephan", "4", "44", "44"],
["Philip", "5", "55", "55"],
["Robert", "6", "66", "66"],
["Andrei", "7", "77", "77"]
]
dataframe = pd.DataFrame(dataset, columns=['Name', 'Value1', 'Value2', 'Value3'])

X = dataframe[['Value1', 'Value2']]
y = dataframe['Value3']

linearregression = linear_model.LinearRegression()
linearregression.fit(X.values, y.values)

predictedvalue= linearregression.predict([[10, 100]])

print(predictedvalue)
