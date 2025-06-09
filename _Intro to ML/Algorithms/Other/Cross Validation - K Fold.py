import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

Age = np.array([39, 40, 41, 48, 49, 50, 51, 52, 54, 55, 36, 37, 42, 43, 44, 45, 47, 50, 53, 54, 35, 36, 37, 38, 40, 41,
                42, 46, 47, 53, 35, 37, 38, 39, 42, 43, 44, 45, 46, 48, 37, 42, 43, 44, 46, 47, 49, 50, 53,
                54]).reshape((-1, 1))
Output = np.array([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0,
                   0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])


kf = KFold(n_splits=10, shuffle=True, random_state=42)

logistic_regression = LogisticRegression()


scores = cross_val_score(logistic_regression, Age, Output, cv=kf, scoring='accuracy')

average_accuracy = np.mean(scores)
print(f'Average_Accuracy: {average_accuracy}')