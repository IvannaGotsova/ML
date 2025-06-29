from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

elementsRandom = random.binomial(n=10, p=0.8, size=50)

print(elementsRandom)

sns.distplot(random.binomial(n=10, p=0.8, size=50), hist=True, kde=False)

plt.show()