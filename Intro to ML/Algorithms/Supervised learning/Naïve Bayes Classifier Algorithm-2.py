import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import LabelEncoder
from webencodings import labels
from sklearn.metrics import classification_report

datasetExampleFiltered = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Outlook': ["Sunny", "Overcast", "Rainy", "Rainy", "Overcast", "Sunny", "Rainy", "Sunny", "Overcast", "Rainy"],
    'Temperature': ["Hot", "Hot", "Cold", "Cold", "Mild", "Mild", "Cold", "Hot", "Mild", "Cold"],
    'Humidity': ["High", "High", "Normal", "Normal", "High", "High", "Normal", "High", "High", "Normal"],
    'Wind': ["No", "Yes", "Yes", "Yes", "No", "No", "No", "Yes", "No", "No"]
}

dataframeExampleFiltered = pd.DataFrame(datasetExampleFiltered)

Numerics = LabelEncoder()

dataframeExampleFiltered['Outlook_numeric'] = Numerics.fit_transform(dataframeExampleFiltered['Outlook'])
dataframeExampleFiltered['Temperature_numeric'] = Numerics.fit_transform(dataframeExampleFiltered['Temperature'])
dataframeExampleFiltered['Humidity_numeric'] = Numerics.fit_transform(dataframeExampleFiltered['Humidity'])
dataframeExampleFiltered['Wind_numeric'] = Numerics.fit_transform(dataframeExampleFiltered['Wind'])

dataframeExampleFiltered_numeric=dataframeExampleFiltered.drop(['Outlook', 'Temperature', 'Humidity', 'Wind'], axis = 'columns')


dataframeExamplePromotion = ["No", "Yes", "No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No"]

print(dataframeExampleFiltered_numeric)

X_train, X_test, y_train, y_test = train_test_split(dataframeExampleFiltered_numeric, dataframeExamplePromotion, test_size=0.50,
                                                    random_state=0)

gaussianNaiveBayesClassifier = GaussianNB()

gaussianNaiveBayesClassifier.fit(X_train, y_train)

y_prediction = gaussianNaiveBayesClassifier.predict(X_test)

accuracy = np.sum(y_prediction == y_test) / len(y_test)
print("Accuracy:", accuracy)


print(classification_report(y_test,y_prediction))
