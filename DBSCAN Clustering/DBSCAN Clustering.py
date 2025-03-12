import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA

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

categorical_columns = dataframe.select_dtypes(include=['object']).columns.tolist()
encoder = OneHotEncoder(sparse_output=False)

one_hot_encoded = encoder.fit_transform(dataframe[categorical_columns])

one_hot_dataframe = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(categorical_columns))

dataframe_encoded = pd.concat([dataframe, one_hot_dataframe], axis=1)

dataframe_encoded = dataframe_encoded.drop(categorical_columns, axis=1)

scaler = StandardScaler()
dataframe_scaled = scaler.fit_transform(dataframe_encoded)

dataframe_normalized = normalize(dataframe_scaled)

dataframe_normalized = pd.DataFrame(dataframe_normalized)

pca = PCA(n_components = 2)
dataframe_transformed = pca.fit_transform(dataframe_normalized)
dataframe_transformed = pd.DataFrame(dataframe_transformed)
dataframe_transformed.columns = ['1', '2']
print(dataframe_transformed.head())

dbscan_model = DBSCAN(eps = 0.0375, min_samples = 2).fit(dataframe_transformed)

plt.figure(figsize=(9, 9))
plt.scatter(dataframe_transformed['1'], dataframe_transformed['2'])
plt.show()

