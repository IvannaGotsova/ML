import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


datasetExample = {
  'First Name': ["Ivan", "Petar", "Dimitar", "Stoqn", "Philip", "Stephan"],
  'Last Name': ["Ivanov", "Petrov", "Dimitrov", "Stoqnov", "Philipov", "Stephanov"],
  'Age': [39, 43, 47, 42, 39, 36],
  'City': ["Sofia", "Sofia", "Plovdiv", "Sofia", "Sofia", "Varna"],
  'Salary': [1000, 1100, 1000, 1000, 1100, 1000],
  'Experience': [10, 15, 17, 14, 11, 5],
  'Grades': [4, 5, 6, 5, 4, 4]
}

datasetExampleFiltered = {
  'Age': [39, 43, 47, 42, 39, 36],
  'Salary': [1000, 1100, 1000, 1000, 1100, 1000],
  'Experience': [10, 15, 17, 14, 11, 5],
  'Grades': [4, 5, 6, 5, 4, 4]
}

dataframeExampleFiltered = pd.DataFrame(datasetExampleFiltered)

dataframeExamplePromotion = ["No", "Yes", "Yes", "Yes", "No", "No"]

print(dataframeExampleFiltered)

X_train, X_test, y_train, y_test = train_test_split(dataframeExampleFiltered, dataframeExamplePromotion, test_size=0.25, random_state=0)

gaussianNaiveBayesClassifier = GaussianNB()

gaussianNaiveBayesClassifier.fit(X_train, y_train)

y_prediction = gaussianNaiveBayesClassifier.predict(X_test)

accuracy = np.sum(y_prediction == y_test) / len(y_test)
print("Accuracy:", accuracy)

confusionMatrix = confusion_matrix(y_test, y_prediction)

print(confusionMatrix)

labels = ["label1", "label2"]

disp = ConfusionMatrixDisplay(confusion_matrix=confusionMatrix, display_labels=labels)
disp.plot()
disp.show()
