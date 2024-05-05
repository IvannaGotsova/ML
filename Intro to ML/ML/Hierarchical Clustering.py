import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

x = [14, 7, 1, 8, 7, 16, 15 , 6, 9, 2]
y = [12, 21, 14, 7, 17, 15, 24, 22, 21, 11]

dataset = list(zip(x, y))

linkageData = linkage(dataset, method='ward', metric='euclidean')
dendrogram(linkageData)

plt.show()