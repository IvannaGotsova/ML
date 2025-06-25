import numpy
from scipy import stats

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

meanVariable = numpy.mean(numbers)
medianVariable = numpy.median(numbers)
modeVariable = stats.mode(numbers)

print(meanVariable)
print(medianVariable)
print(modeVariable)

