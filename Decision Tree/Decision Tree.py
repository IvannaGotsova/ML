import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

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

# Encoding

categorical_columns = dataframe.select_dtypes(include=['object']).columns.tolist()
encoder = OneHotEncoder(sparse_output=False)

one_hot_encoded = encoder.fit_transform(dataframe[categorical_columns])

one_hot_dataframe = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(categorical_columns))

dataframe_encoded = pd.concat([dataframe, one_hot_dataframe], axis=1)

dataframe_encoded = dataframe_encoded.drop(categorical_columns, axis=1)

print(one_hot_dataframe)

# Decision Tree

decision_tree = DecisionTreeClassifier()
attributes = dataframe_encoded.drop(columns='Score')
target = dataframe_encoded['Score']
decision_tree = decision_tree.fit(attributes, target)

# Plotting

tree.plot_tree(decision_tree, feature_names=dataframe_encoded.columns)

tree_representation = tree.export_text(decision_tree)
print(tree_representation)

tree_figure = plt.figure(figsize=(25, 25))
tree.plot_tree(decision_tree,
               feature_names=None,
               class_names=None,
               filled=True)

tree_figure.savefig("decistion_tree.png")