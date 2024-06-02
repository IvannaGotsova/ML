import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

x = [1, 2, 71, 89, 98, 100, 10, 9, 3, 66]
y = [11, 28, 1, 2, 7, 34, 43, 57, 65, 99, 39]

data = list(zip(x, y))
inertias = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,11), inertias, marker='o')
plt.title('Data Title')
plt.xlabel('x')
plt.ylabel('y')
plt.show()