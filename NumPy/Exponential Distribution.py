from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

elementsRandom = random.exponential(size=100)

print(elementsRandom)

sns.distplot(elementsRandom, hist=False)

plt.show()