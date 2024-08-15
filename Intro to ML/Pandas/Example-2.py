import pandas as pd
import matplotlib.pyplot as plt

datasetExample = {
    'First Name': ["Ivan", "Petar", "Dimitar", "Stoqn", "Philip", "Stephan"],
    'Last Name': ["Ivanov", "Petrov", "Dimitrov", "Stoqnov", "Philipov", "Stephanov"],
    'Age': [39, 43, 47, 42, 39, 36],
    'City': ["Sofia", "Sofia", "Plovdiv", "Sofia", "Sofia", "Varna"],
    'Salary': [1000, 1100, 1000, 1000, 1100, 1000],
    'Experience': [10, 15, 17, 14, 11, 5],
    'Grades': [4, 5, 6, 5, 4, 4]
}

dataframeExample = pd.DataFrame(datasetExample)

print(dataframeExample['First Name'].value_counts())
print()
print(len(dataframeExample))
print()
print(dataframeExample.shape)
print()
print(dataframeExample.describe())
print()
print(dataframeExample.min())
print()
print(dataframeExample.max())
print()
print(dataframeExample['Age'].mean())
print()
print(dataframeExample['Age'].median())
print()
print(dataframeExample.count())
print()
print(dataframeExample['Age'].var())
print()
print(dataframeExample['Age'].std())
print()
dataframeExample.plot.scatter(x="Age", y="City")
dataframeExample.plot.scatter(x="Age", y="Salary")
" plt.show() "

datasetExampleNew = {
    'First Name': ["Ivan", "Petar", "Dimitar", "Stoqn", "Philip", "Stephan"],
    'Last Name': ["Ivanov", "Petrov", "Dimitrov", "Stoqnov", "Philipov", "Stephanov"],
    'Age': [39, 43, 47, 42, 39, 36],
    'City': ["Sofia", "Sofia", "Plovdiv", "Sofia", "Sofia", "Varna"],
    'Salary': [1000, 1100, 1000, 1000, 1100, 1000],
    'Experience': [10, 15, 17, 14, 11, 5],
    'Grades': [4, 5, 6, 5, 4, 4],
    'Result': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes'],
}

dataframeExampleNew = pd.DataFrame(datasetExampleNew)

dataframeExampleMerge = pd.merge(dataframeExample, dataframeExampleNew)
print(dataframeExampleMerge)
print()

dataframeExampleFiltered = dataframeExample[['Age', 'Salary', 'Experience', 'Grades']]
print(dataframeExampleFiltered)
print()

print(dataframeExampleFiltered.corr())
print()

dataframeExample = pd.DataFrame(dataframeExample, index=[1, 2, 3, 4, 5, 6])
print(dataframeExample)
