import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


datasetExample = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55,
            56, 57, 58, 59, 60],
    'Outlook': ["Sunny", "Overcast", "Rainy", "Rainy", "Overcast", "Sunny", "Rainy", "Sunny", "Overcast", "Rainy",
                "Overcast", "Sunny", "Rainy", "Sunny", "Overcast", "Rainy", "Sunny", "Rainy", "Sunny", "Overcast",
                "Sunny", "Rainy", "Sunny", "Overcast", "Rainy", "Overcast", "Sunny", "Rainy", "Sunny", "Overcast",
                "Overcast", "Sunny", "Rainy", "Sunny", "Overcast", "Rainy", "Sunny", "Rainy", "Sunny", "Overcast",
                "Overcast", "Sunny", "Rainy", "Sunny", "Overcast", "Rainy", "Sunny", "Rainy", "Sunny", "Overcast",
                "Overcast", "Sunny", "Rainy", "Sunny", "Overcast", "Rainy", "Sunny", "Rainy", "Sunny", "Overcast"],
    'Temperature': ["Hot", "Hot", "Cold", "Cold", "Mild", "Mild", "Cold", "Hot", "Mild", "Cold",
                    "Hot", "Cold", "Cold", "Mild", "Mild", "Hot", "Cold", "Cold", "Mild", "Mild",
                    "Hot", "Cold", "Cold", "Mild", "Mild", "Hot", "Cold", "Cold", "Mild", "Mild",
                    "Hot", "Hot", "Cold", "Cold", "Mild", "Mild", "Cold", "Hot", "Mild", "Cold",
                    "Hot", "Hot", "Cold", "Cold", "Mild", "Mild", "Cold", "Hot", "Mild", "Cold",
                    "Hot", "Cold", "Cold", "Mild", "Mild", "Hot", "Cold", "Cold", "Mild", "Mild"],
    'Humidity': ["High", "High", "Normal", "Normal", "High", "High", "Normal", "High", "High", "Normal",
                 "High", "High", "Normal", "Normal", "High", "High", "Normal", "High", "High", "Normal",
                 "Normal", "Normal", "High", "Normal", "Normal", "High", "Normal", "Normal", "High", "Normal",
                 "High", "High", "Normal", "Normal", "High", "High", "Normal", "High", "High", "Normal",
                 "High", "High", "Normal", "Normal", "High", "High", "Normal", "High", "High", "Normal",
                 "Normal", "Normal", "High", "Normal", "Normal", "High", "Normal", "Normal", "High", "Normal"],
    'Wind': ["No", "Yes", "Yes", "Yes", "No", "No", "No", "Yes", "No", "No",
             "No", "Yes", "No", "No", "Yes", "Yes", "Yes", "No", "No", "Yes",
             "Yes", "Yes", "Yes", "No", "No", "Yes", "Yes", "Yes", "No", "No",
             "Yes", "Yes", "Yes", "No", "No", "Yes", "Yes", "Yes", "No", "No",
             "Yes", "Yes", "Yes", "No", "No", "Yes", "Yes", "Yes", "No", "No",
             "No", "Yes", "No", "No", "Yes", "Yes", "Yes", "No", "No", "Yes"],
    'Predicted': ["No", "Yes", "No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No",
                  "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes", "Yes", "No", "Yes",
                  "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "No", "No",
                  "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes", "Yes", "No", "Yes",
                  "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes", "Yes", "No", "Yes",
                  "No", "Yes", "No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No"
                  ]
}


dataframeExample = pd.DataFrame(datasetExample)

resultConvertOutlook = {'Sunny': 0, 'Overcast': 1, 'Rainy': 2}
resultConvertTemperature = {'Hot': 0, 'Cold': 1, 'Mild': 2}
resultConvertHumidity = {'High': 0, 'Normal': 1}
resultConvertWind = {'Yes': 0, 'No': 1}
resultConvertPredicted = {'Yes': 0, 'No': 1}

dataframeExample['Outlook'] = dataframeExample['Outlook'].map(resultConvertOutlook)
dataframeExample['Temperature'] = dataframeExample['Temperature'].map(resultConvertTemperature)
dataframeExample['Humidity'] = dataframeExample['Humidity'].map(resultConvertHumidity)
dataframeExample['Wind'] = dataframeExample['Wind'].map(resultConvertWind)
dataframeExample['Predicted'] = dataframeExample['Predicted'].map(resultConvertPredicted)

dataframeExample = pd.get_dummies(dataframeExample)

training_data = dataframeExample[['Day', 'Outlook', 'Temperature', 'Humidity', 'Wind']]
testing_data = dataframeExample["Predicted"]

X_train, X_test, y_train, y_test = train_test_split(training_data, testing_data, test_size=0.25, random_state=67)

sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

pca = PCA(n_components=2)

X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

explained_variance = pca.explained_variance_ratio_

classifier = LogisticRegression(random_state=1)
classifier.fit(X_train, y_train)
y_prediction = classifier.predict(X_test)

