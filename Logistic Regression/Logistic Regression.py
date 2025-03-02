import pandas as pd
from sklearn import linear_model

dataset = [
["Ivan", "Plovdiv", "Mathematics", "22", "6", "91.2", 1],
["Petar", "Sofia", "Biology","35", "5", "63.5", 0],
["Dimitar", "Varna", "Mathematics","43", "5", "90.23", 0],
["Stephan", "Burgas","Computer Science", "45", "4", "92.7", 1],
["Philip", "Sofia", "Statistics","49", "6", "98.2", 1],
["Robert", "Sofia", "Mathematics","23", "3", "88.1", 1],
["Andrei", "Plovdiv", "Biology","34", "4", "95.0", 0]
]

dataframe = pd.DataFrame(dataset, columns=['Name', "City", 'Subject', 'Age', 'Grade', 'Percentage', "Score"])

dataframe = dataframe.drop(columns='Name')
dataframe = pd.get_dummies(dataframe, columns=['City', 'Subject'], drop_first=True)

print(dataframe)

attributes = dataframe.drop(columns='Score')
target = dataframe['Score']

print(attributes)
print()
print(target)
print()

logistic_regression = linear_model.LogisticRegression()
logistic_regression.fit(attributes, target)
predictions = logistic_regression.predict(attributes)
print(predictions)
print()

print(logistic_regression.score(attributes, target))