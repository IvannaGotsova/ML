import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn import tree
from sklearn.svm import SVC
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

# SVM

attributes = dataframe_encoded.drop(columns='Score')
target = dataframe_encoded['Score']

attributes_train, attributes_test, target_train, target_test = train_test_split(attributes, target,
                                                                                test_size=0.33, random_state=42)

svm = SVC(kernel='linear')

svm.fit(attributes_train, target_train)

predictions = svm.predict(attributes_test)

accuracy = accuracy_score(target_test, predictions)
print("Accuracy:", accuracy)