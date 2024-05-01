import pandas
import pandas as pd
from sklearn import linear_model

dataset = [
["Ivan", "Plovdiv", "Mathematics", "22", "6", "91.2"],
["Petar", "Sofia", "Biology","35", "5", "63.5"],
["Dimitar", "Varna", "Mathematics","43", "5", "90.23"],
["Stephan", "Burgas","Computer Science", "45", "4", "92.7"],
["Philip", "Sofia", "Statistics","49", "6", "98.2"],
["Robert", "Sofia", "Mathematics","23", "3", "88.1"],
["Andrei", "Plovdiv", "Biology","34", "4", "95.0"]
]

dataframe = pd.DataFrame(dataset, columns=['Name', "City", 'Subject', 'Age', 'Grade', 'Percentage'])

dataframeTwo = pd.get_dummies(dataframe[['Subject']])

X = pd.concat([dataframe[['Age', 'Grade']], dataframeTwo], axis=1)
y = dataframe['Percentage']

linearRegression = linear_model.LinearRegression()
linearRegression.fit(X,y)

predictedPercentage = linearRegression.predict([[23, 3, 0, 0, 1, 0]])

print(predictedPercentage)