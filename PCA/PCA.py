import pandas as pd
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder, StandardScaler

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

scaling = StandardScaler()

scaling.fit(dataframe_encoded)
Scaled_data = scaling.transform(dataframe_encoded)

principal = PCA(n_components=2)
principal.fit(Scaled_data)
x = principal.transform(Scaled_data)

print(x.shape)
print(x)