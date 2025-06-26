import numpy
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [11, 28, 34, 43, 57, 65, 71, 89, 98, 100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 10, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()