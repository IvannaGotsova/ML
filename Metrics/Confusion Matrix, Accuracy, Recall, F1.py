import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

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
print()

attributes = dataframe.drop(columns='Score')
target = dataframe['Score']

attributes_train, attributes_test, target_train, target_test = train_test_split(attributes, target,
                                                                                test_size=0.33, random_state=42)

print(attributes_train)
print(attributes_test)
print(target_train)
print(target_test)
print()

linear_regression_model = LinearRegression()
linear_regression_model.fit(attributes_train, target_train)
predictions = linear_regression_model.predict(attributes_test)
predictions = np.where(predictions > 0.5, 1, 0)

print(predictions)
print()

confusion_matrix = metrics.confusion_matrix(target_test, predictions)
confusion_matrix_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [0, 1])

confusion_matrix_display.plot()
plt.show()

print("Accuracy")
print(metrics.accuracy_score(target_test, predictions))
print("Recall")
print(metrics.recall_score(target_test, predictions))
print("F1")
print(metrics.f1_score(target_test, predictions))
print("Precision")
print(metrics.precision_score(target_test, predictions))
print("Specificity")
print(metrics.recall_score(target_test, predictions, pos_label=0))