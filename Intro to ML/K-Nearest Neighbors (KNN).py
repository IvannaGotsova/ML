import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
classes = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

data = list(zip(x, y))
print(data)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(data, classes)

newX = 5.5
newY = 55
newPoint = [(newX, newY)]
prediction = knn.predict(newPoint)
print(prediction)

plt.scatter(x + [newX], y + [newY], c=classes + [prediction[0]])
plt.text(x=newX-0, y=newY-0, s=f"new point, class: {prediction[0]}")
plt.show()