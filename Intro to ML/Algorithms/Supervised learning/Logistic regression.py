import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split

Age = np.array([39, 40, 41, 48, 49, 50, 51, 52, 54, 55, 36, 37, 42, 43, 44, 45, 47, 50, 53, 54, 35, 36, 37, 38, 40, 41,
                42, 46, 47, 53, 35, 37, 38, 39, 42, 43, 44, 45, 46, 48, 37, 42, 43, 44, 46, 47, 49, 50, 53,
                54]).reshape((-1, 1))
Output = np.array([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0,
                   0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

plt.scatter(Age, Output)
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age / Salary")
plt.plot(Age, Output, color="b")
plt.legend(["Age - Salary"], loc="right")
#plt.show()

X_train, X_test, y_train, y_test = train_test_split(Age, Output, test_size=0.2, random_state=42)

plt.scatter(X_train, y_train)
plt.xlabel("Train")
plt.ylabel("Test")
plt.title("Train / Test")
plt.plot(X_train, y_train, color="b")
plt.legend(["Train - Test"], loc="right")
plt.show()

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
