import numpy
import matplotlib.pyplot as plt
from sklearn import metrics

actualValues = numpy.random.binomial(1, 0.5, size = 1000)
predictedValues = numpy.random.binomial(1, 0.5, size = 1000)

confusionMatrix = metrics.confusion_matrix(actualValues, predictedValues)

confusionMatrixDisplay = metrics.ConfusionMatrixDisplay(confusion_matrix = confusionMatrix, display_labels = [0, 1])

confusionMatrixDisplay.plot()
plt.show()

accuracy = metrics.accuracy_score(actualValues, predictedValues)
precision = metrics.precision_score(actualValues, predictedValues)
sensitivityRecall = metrics.recall_score(actualValues, predictedValues)
specificity = metrics.recall_score(actualValues, predictedValues, pos_label=0)
f1Score = metrics.f1_score(actualValues, predictedValues)

print(accuracy)
print(precision)
print(sensitivityRecall)
print(specificity)
print(f1Score)

