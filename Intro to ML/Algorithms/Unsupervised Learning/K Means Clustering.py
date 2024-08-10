import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

x = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 41, 42, 42, 43, 44, 44, 44, 44, 46, 46, 89, 89, 90, 91, 92, 92, 94, 94, 96, 99]
y = [6, 8, 8, 7, 7, 7, 5, 6, 9, 9, 21, 21, 21, 29, 29, 29, 30, 31, 32, 33, 71, 71, 71, 73, 73, 75, 75, 77, 78, 79]

data = list(zip(x, y))

kmeans = KMeans(n_clusters=6)
kmeans.fit(data)

plt.scatter(x, y, c=kmeans.labels_)
plt.show()