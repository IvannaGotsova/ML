import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

Age = [39, 40, 41, 48, 49, 50, 51, 52, 54, 55, 36, 37, 42, 43, 44, 45, 47, 50, 53, 54, 35, 36, 37, 38, 40, 41, 42, 46, 47, 53, 35, 37, 38, 39, 42, 43, 44, 45, 46, 48, 37, 42, 43, 44, 46, 47, 49, 50, 53, 54]
Salary = [ 1064, 1067, 1079, 1081, 1110, 1116, 1178, 1208, 1269, 1276, 1303, 1354, 1437, 1472, 1489, 1495, 1515, 1529, 1571, 1580, 1603, 1626, 1638, 1664, 1694, 1699, 1723, 1766, 1768, 1771, 1781, 1783, 1784, 1804, 1834, 1840, 1874, 1895, 1901, 1905, 1913, 1947, 1953, 1955, 1957, 1960, 1961, 1975, 1989, 1995]

plt.scatter(Age, Salary)
plt.xlabel("Age")
plt.ylabel("Salary")
plt.plot(Age, Salary, color = "b")
#plt.show()


X_train, X_test,\
  y_train, y_test = train_test_split(Age, Salary,
                    test_size=0.4,
                    random_state=1)


linear_model = linear_model.LinearRegression()
linear_model.fit(X_train, y_train)


