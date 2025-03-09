import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsClassifier

dataset = [
["Ivan", "Plovdiv", "Mathematics", "22", "6", "91.2", 1],
["Petar", "Sofia", "Biology","35", "5", "63.5", 0],
["Dimitar", "Varna", "Mathematics","43", "5", "90.23", 0],
["Stephan", "Burgas","Computer Science", "45", "4", "92.7", 1],
["Philip", "Sofia", "Statistics","49", "6", "98.2", 1],
["Robert", "Sofia", "Mathematics","23", "3", "88.1", 1],
["Andrei", "Plovdiv", "Biology","34", "4", "95.0", 0]
]

dataframe = pd.DataFrame(dataset, columns=['Name', "City", 'Subject', 'Age', 'Grade', 'Percentage', "Score"])


new_Grade = dataframe["Grade"].astype(int)
new_Percentage = dataframe["Percentage"].astype(float)

data = list(zip(new_Grade, new_Percentage))
classes = dataframe["Score"]

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(data, classes)

new_Grade_X = 5
new_Percentage_Y = 95.0
newPoint = [(new_Grade_X, new_Percentage_Y)]
prediction = knn.predict(newPoint)
print(prediction)

plt.scatter(new_Grade + [new_Grade_X], new_Percentage + [new_Percentage_Y], c=classes + [prediction[0]])
plt.text(x=new_Grade_X-0, y=new_Percentage_Y-0, s=f"new point, class: {prediction[0]}")
plt.show()