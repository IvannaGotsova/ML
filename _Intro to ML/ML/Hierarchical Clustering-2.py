import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

x = [14, 7, 1, 8, 7, 16, 15 , 6, 9, 2]
y = [12, 21, 14, 7, 17, 15, 24, 22, 21, 11]

dataset = list(zip(x, y))

hierarchicalCluster = AgglomerativeClustering(n_clusters=2, linkage='ward')
labels = hierarchicalCluster.fit_predict(dataset)

plt.scatter(x, y, c=labels)
plt.show()