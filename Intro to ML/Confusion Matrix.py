import numpy
import matplotlib.pyplot as plt
from sklearn import metrics

actualValues = numpy.random.binomial(1, 0.5, size = 1000)
predictedValues = numpy.random.binomial(1, 0.5, size = 1000)

confusionMatrix = metrics.confusion_matrix(actualValues, predictedValues)

confusionMatrixDisplay = metrics.ConfusionMatrixDisplay(confusion_matrix = confusionMatrix, display_labels = [0, 1])

confusionMatrixDisplay.plot()
plt.show()