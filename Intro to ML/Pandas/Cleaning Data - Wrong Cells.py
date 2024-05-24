import pandas as pd

datasetExample = {
    'First Name': ["Ivan", "Petar", "Dimitar", "Stoqn", "Philip", "Stephan"],
    'Last Name': ["Ivanov", "Petrov", "Dimitrov", "Stoqnov", "Philipov", "Stephanov"],
    'age': [39, 43, 47, 42, 39, 36],
    'city': ["Sofia", "Sofia", "Plovdiv", "Sofia", "Sofia", "Varna"],
    'salary': [1000, 1100, 1000, 1000, 1100, 1000],
    'grades': [4.1, 5.3, 6.3, 5.4, 4.7, 4.3]
}

dataframeExample = pd.DataFrame(datasetExample, index = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth"])

dataframeExample['grades'] = pd.DataFrame(dataframeExample['grades'].astype(int))
print(dataframeExample)
print()
