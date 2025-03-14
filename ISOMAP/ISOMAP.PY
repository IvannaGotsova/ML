import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.manifold import Isomap
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

attributes = dataframe.drop(columns='Score')
target = dataframe['Score']

categorical_columns = attributes.select_dtypes(include=['object']).columns.tolist()
encoder = OneHotEncoder(sparse_output=False)

one_hot_encoded = encoder.fit_transform(dataframe[categorical_columns])

one_hot_dataframe = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(categorical_columns))

attributes_dataframe_encoded = pd.concat([dataframe, one_hot_dataframe], axis=1)

attributes_dataframe_encoded = attributes_dataframe_encoded.drop(categorical_columns, axis=1)

scaler_model = StandardScaler()
dataframe_scaled = scaler_model.fit_transform(attributes_dataframe_encoded)

dataframe_isomap = Isomap(n_neighbors=5, n_components=2)
dataframe_transformed = dataframe_isomap.fit_transform(dataframe_scaled)