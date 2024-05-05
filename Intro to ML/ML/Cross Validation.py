import pandas as pd
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold, cross_val_score


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
y = dataframe['Percentage']

decisionTreeClassifier = DecisionTreeClassifier(random_state=42)

kFolds = KFold(n_splits = 5)

crossValidationScores = cross_val_score(decisionTreeClassifier, X, y, cv = kFolds)

print("Cross Validation: ", crossValidationScores)
print("Average Cross Validation: ", crossValidationScores.mean())
print("Number of Cross Validati in Average: ", len(crossValidationScores))