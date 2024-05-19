from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

elementsRandom = random.poisson(lam=5, size=100),

print(elementsRandom)

sns.distplot(elementsRandom, kde=False)

plt.show()