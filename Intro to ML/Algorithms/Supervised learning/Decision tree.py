import sys
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

datasetExample = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Outlook': ["Sunny", "Overcast", "Rainy", "Rainy", "Overcast", "Sunny", "Rainy", "Sunny", "Overcast", "Rainy"],
    'Temperature': ["Hot", "Hot", "Cold", "Cold", "Mild", "Mild", "Cold", "Hot", "Mild", "Cold"],
    'Humidity': ["High", "High", "Normal", "Normal", "High", "High", "Normal", "High", "High", "Normal"],
    'Wind': ["No", "Yes", "Yes", "Yes", "No", "No", "No", "Yes", "No", "No"],
    'Predicted': ["No", "Yes", "No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No"]
}

dataframeExample = pd.DataFrame(datasetExample)

resultConvertOutlook = {'Sunny': 0, 'Overcast': 1, 'Rainy': 2}
resultConvertTemperature = {'Hot': 0, 'Cold': 1, 'Mild': 2}
resultConvertHumidity = {'High': 0, 'Normal': 1}
resultConvertWind = {'Yes': 0, 'No': 1}
resultConvertPredicted = {'Yes': 0, 'No': 1}

dataframeExample['Outlook'] = dataframeExample['Outlook'].map(resultConvertOutlook)
dataframeExample['Temperature'] = dataframeExample['Temperature'].map(resultConvertTemperature)
dataframeExample['Humidity'] = dataframeExample['Humidity'].map(resultConvertHumidity)
dataframeExample['Wind'] = dataframeExample['Wind'].map(resultConvertWind)
dataframeExample['Predicted'] = dataframeExample['Predicted'].map(resultConvertPredicted)

features = ['Outlook', 'Temperature', 'Humidity', 'Wind']

X = dataframeExample[features]
y = dataframeExample['Predicted']

decisionTree = DecisionTreeClassifier()
decisionTree = decisionTree.fit(X, y)

tree.plot_tree(decisionTree, feature_names=features)

tree_representation = tree.export_text(decisionTree)
print(tree_representation)

tree_figure = plt.figure(figsize=(25, 25))
tree.plot_tree(decisionTree,
               feature_names=None,
               class_names=None,
               filled=True)

tree_figure.savefig("decistion_tree.png")