import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split

Age = np.array([39, 40, 41, 48, 49, 50, 51, 52, 54, 55, 36, 37, 42, 43, 44, 45, 47, 50, 53, 54, 35, 36, 37, 38, 40, 41,
                42, 46, 47, 53, 35, 37, 38, 39, 42, 43, 44, 45, 46, 48, 37, 42, 43, 44, 46, 47, 49, 50, 53,
                54]).reshape((-1, 1))
Output = np.array([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0,
                   0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]).reshape((-1, 1))

plt.scatter(Age, Output)
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age / Salary")
plt.plot(Age, Output, color="b")
plt.show()

logistic_regression = linear_model.LogisticRegression()
logistic_regression.fit(Age, Output)

X_train, X_test, y_train, y_test = train_test_split(Age, Output,
                                                    test_size=0.2,
                                                    random_state=1)
