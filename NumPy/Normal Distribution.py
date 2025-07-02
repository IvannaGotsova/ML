from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

elementsRandom = random.normal(loc=10, scale=0.01, size=(20))

print(elementsRandom)

sns.distplot(elementsRandom, hist=False)

plt.show()