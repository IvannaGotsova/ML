import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 15, 25])

plt.pie(y, labels = ['One', 'Two', 'Three', 'Four'])
plt.show()