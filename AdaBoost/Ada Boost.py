import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class AdaBoost:
    def __init__(self, n_estimators=50):
        self.n_estimators = n_estimators
        self.alphas = []
        self.models = []

    def fit(self, x, y):
        n_samples, n_features = x.shape
        w = np.ones(n_samples) / n_samples

    def predict(self, X):
        strong_preds = np.zeros(X.shape[0])
        for model, alpha in zip(self.models, self.alphas):
            strong_preds += alpha * model.predict(X)
        return np.sign(strong_preds).astype(int)


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

adaboost = AdaBoost(n_estimators=50)

adaboost.fit(attributes_train, target_train)

predictions = adaboost.predict(attributes_test)

print(target_test)
print(predictions)
print(accuracy_score(target_test, predictions))
