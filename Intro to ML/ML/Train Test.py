import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

numpy.random.seed(2)

x = numpy.random.normal(5, 5, 500)
y = numpy.random.normal(100, 20, 500)

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(train_y, mymodel(train_x))
print(r2)

r2 = r2_score(test_y, mymodel(test_x))
print(r2)

print(mymodel(35))

myline = numpy.linspace(-10, 20, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()