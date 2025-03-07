import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

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

attributes = dataframe.drop(columns='Score')
target = dataframe['Score']

logistic_regression = LogisticRegression(max_iter = 100000)

C = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]

scores = []

for c in C:
  logistic_regression.set_params(C=c)
  logistic_regression.fit(attributes, target)
  scores.append(logistic_regression.score(attributes, target))

print(scores)

