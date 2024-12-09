import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier

pd.set_option('future.no_silent_downcasting', True)

datasetExample = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Outlook': ["Sunny", "Overcast", "Rainy", "Rainy", "Overcast", "Sunny", "Rainy", "Sunny", "Overcast", "Rainy",
                "Overcast", "Sunny", "Rainy", "Sunny", "Overcast", "Rainy", "Sunny", "Rainy", "Sunny", "Overcast",
                "Sunny", "Rainy", "Sunny", "Overcast", "Rainy", "Overcast", "Sunny", "Rainy", "Sunny", "Overcast"],
    'Temperature': ["Hot", "Hot", "Cold", "Cold", "Mild", "Mild", "Cold", "Hot", "Mild", "Cold",
                    "Hot", "Cold", "Cold", "Mild", "Mild", "Hot", "Cold", "Cold", "Mild", "Mild",
                    "Hot", "Cold", "Cold", "Mild", "Mild", "Hot", "Cold", "Cold", "Mild", "Mild"],
    'Humidity': ["High", "High", "Normal", "Normal", "High", "High", "Normal", "High", "High", "Normal",
                 "High", "High", "Normal", "Normal", "High", "High", "Normal", "High", "High", "Normal",
                 "Normal", "Normal", "High", "Normal", "Normal", "High", "Normal", "Normal", "High", "Normal"],
    'Wind': ["No", "Yes", "Yes", "Yes", "No", "No", "No", "Yes", "No", "No",
             "No", "Yes", "No", "No", "Yes", "Yes", "Yes", "No", "No", "Yes",
             "Yes", "Yes", "Yes", "No", "No", "Yes", "Yes", "Yes", "No", "No"],
    'Predicted': ["No", "Yes", "No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No",
                  "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes", "Yes", "No", "Yes",
                  "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "No", "No"]
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


X = dataframeExample[['Day', 'Outlook', 'Temperature', 'Humidity', 'Wind']]
Y = dataframeExample["Predicted"]


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)


model = XGBClassifier()
model.fit(X_train, y_train)

prediction = model.predict(X_test)
predictions = [round(value) for value in prediction]

accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))