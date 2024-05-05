import numpy
import matplotlib.pyplot as plt

dataVariable = numpy.random.uniform(0.0, 10.0, 20)

plt.hist(dataVariable, 10)
plt.show()