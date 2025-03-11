import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


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


grade = dataframe["Grade"]
percentage = dataframe["Percentage"]

plt.scatter(grade, percentage)
plt.show()


data = list(zip(grade, percentage))
inertias = []

for i in range(1,8):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,8), inertias, marker='o')
plt.show()


kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

plt.scatter(grade, percentage, c=kmeans.labels_)
plt.show()