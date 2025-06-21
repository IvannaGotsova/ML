import numpy
import matplotlib.pyplot as plt

dataVariable = numpy.random.uniform(0.0, 10.0, 2000)

plt.hist(dataVariable, 1000)
plt.show()