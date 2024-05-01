import numpy
from sklearn import linear_model

X = numpy.array([1, 5, 2, 4, 7, 6, 27, 37, 46, 52, 39, 58]).reshape(-1,1)
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()
logr.fit(X,y)

predictedOne = logr.predict(numpy.array([8]).reshape(-1,1))
print(predictedOne)

predictedOne = logr.predict(numpy.array([0]).reshape(-1,1))
print(predictedOne)

predictedOne = logr.predict(numpy.array([10]).reshape(-1,1))
print(predictedOne)

predictedOne = logr.predict(numpy.array([111]).reshape(-1,1))
print(predictedOne)

predictedOne = logr.predict(numpy.array([61]).reshape(-1,1))
print(predictedOne)