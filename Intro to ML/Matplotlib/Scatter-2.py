import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

x = np.array([0, 1, 3, 5, 7, 9, 10])
y = np.array([0, 2, 4, 6, 8, 9, 10])
x2 = np.array([1, 2, 3, 6, 9, 9, 10])
y2 = np.array([2, 4, 4, 6, 9, 9, 10])
x3 = np.array([0, 1, 2, 5, 6, 8, 10])
y3 = np.array([0, 2, 5, 6, 7, 8, 10])

plt.scatter(x, y)
plt.scatter(x2, y2)
plt.scatter(x3, y3)
plt.show()