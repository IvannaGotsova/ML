import pandas as pd

datasetExample = {
  'First Name': ["Ivan", "Petar", "Dimitar", "Stoqn", "Philip", "Stephan"],
  'Last Name': ["Ivanov", "Petrov", "Dimitrov", "Stoqnov", "Philipov", "Stephanov"],
  'age': [39, 43, 47, 42, 39, 36],
  'city': ["Sofia", "Sofia", "Plovdiv", "Sofia", "Sofia", "Varna"],
  'salary': [1000, 1100, 1000, 1000, 1100, 1000],
  'grades': [4, 5, 6, 5, 4, 4]
}

dataframeExample = pd.DataFrame(datasetExample)

print(dataframeExample)