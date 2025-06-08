import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

x = [44, 42, 43, 44, 45, 36, 37, 38, 39, 30]
y = [2100, 1990, 1800, 1040, 1500, 1500, 1070, 1080, 1500, 1000]
classes = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

data = list(zip(x, y))

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(data, classes)

newX = 44
newY = 1000
newPoint = [(newX, newY)]
prediction = knn.predict(newPoint)
print(prediction)

plt.scatter(x + [newX], y + [newY], c=classes + [prediction[0]])
plt.text(x=newX-0, y=newY-0, s=f"new point, class: {prediction[0]}")
plt.show()