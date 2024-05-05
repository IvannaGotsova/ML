import matplotlib.pyplot as plt
from scipy import stats

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [11, 28, 34, 43, 57, 65, 71, 89, 98, 100]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunction(x):
  return slope * x + intercept

mymodel = list(map(myfunction, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()