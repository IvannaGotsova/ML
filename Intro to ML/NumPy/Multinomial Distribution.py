from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


elementsRandom = random.multinomial(n=10, pvals=[1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10])

print(elementsRandom)

sns.distplot(elementsRandom, hist=False)

plt.show()