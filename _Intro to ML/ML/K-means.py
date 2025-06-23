import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [11, 28, 34, 43, 57, 65, 71, 89, 98, 100]

data = list(zip(x, y))
inertias = []

for i in range(1,10):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,10), inertias, marker='o')
plt.title('Data Title')
plt.xlabel('x')
plt.ylabel('y')
plt.show()