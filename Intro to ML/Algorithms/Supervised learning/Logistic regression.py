import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn import metrics

Age = np.array([39, 40, 41, 48, 49, 50, 51, 52, 54, 55, 36, 37, 42, 43, 44, 45, 47, 50, 53, 54, 35, 36, 37, 38, 40, 41,
                42, 46, 47, 53, 35, 37, 38, 39, 42, 43, 44, 45, 46, 48, 37, 42, 43, 44, 46, 47, 49, 50, 53,
                54]).reshape((-1, 1))
Output = np.array([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0,
                   0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# plt.scatter(Age, Output)
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age / Salary")
plt.plot(Age, Output, color="b")
plt.legend(["Age - Salary"], loc="right")
# plt.show()

X_train, X_test, y_train, y_test = train_test_split(Age, Output, test_size=0.2, random_state=42)

# plt.scatter(X_train, y_train)
plt.xlabel("Train X")
plt.ylabel("Train Y")
plt.title("Train")
plt.plot(X_train, y_train, color="b")
plt.legend(["Train"], loc="right")
# plt.show()

plt.scatter(X_test, y_test)
plt.xlabel("Test")
plt.ylabel("Test")
plt.title("Test")
plt.plot(X_test, y_test, color="b")
plt.legend(["Test"], loc="right")
# plt.show()

print(X_train)
print(y_train)
print(X_test)
print(y_test)
print()

logistic_regression = linear_model.LogisticRegression()
logistic_regression.fit(X_train, y_train)

y_prediction = (logistic_regression.predict(X_test))
print(y_test)
print(y_prediction)
print()

print(logistic_regression.predict(np.array([29]).reshape(-1, 1)))
print(logistic_regression.predict(np.array([37]).reshape(-1, 1)))
print(logistic_regression.predict(np.array([45]).reshape(-1, 1)))
print(logistic_regression.predict(np.array([53]).reshape(-1, 1)))
print(logistic_regression.predict(np.array([65]).reshape(-1, 1)))
print()

print(f"Slope is {logistic_regression.coef_}")
print(f"Intercept is {logistic_regression.intercept_}")
print(f"Coefficient of determination is {logistic_regression.score(Age, Output)}")
print()

accuracy = accuracy_score(y_test, y_prediction)
print(f"Accuracy is {accuracy}")

precision = precision_score(y_test, y_prediction)
print(f"Precision is {precision}")

recall = recall_score(y_test, y_prediction)
print(f"Recall (Sensitivity) is  {recall}:")

f1 = f1_score(y_test, y_prediction)
print(f"F1-Score is {f1}")

confusion_matrix = metrics.confusion_matrix(y_test, y_prediction)
confusion_matrix_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=[0, 1])

confusion_matrix_display.plot()
plt.show()
