import sys

import pandas as pd
from matplotlib import pyplot as plt
from sklearn import tree
from sklearn import linear_model, __all__
from sklearn.tree import DecisionTreeClassifier

dataset = [
["Ivan", "22", "6", "91.2", 'OK'],
["Petar", "35", "5", "63.5", "NO"],
["Dimitar", "43", "5", "90.23", "NO"],
["Stephan", "45", "4", "92.7", "OK"],
["Philip", "49", "6", "98.2", "OK"],
["Robert", "23", "3", "88.1", 'NO'],
["Andrei", "34", "4", "95.0", 'OK'],
]
dataframe = pd.DataFrame(dataset, columns=['Name', 'Age', 'Grade', 'Percentage', "Result"])
resultConvert = {'OK': 0, 'NO': 1}
dataframe['Result'] = dataframe['Result'].map(resultConvert)

features = ['Age', 'Grade', 'Percentage']

X = dataframe[features]
y = dataframe['Result']

decisionTree = DecisionTreeClassifier()
decisionTree = decisionTree.fit(X, y)

tree.plot_tree(decisionTree, feature_names=features)

