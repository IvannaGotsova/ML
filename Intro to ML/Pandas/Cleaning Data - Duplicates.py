import pandas as pd

datasetExample = {
  'First Name': ["Ivan", "Petar", "Dimitar", "Stoqn", "Philip", "Stephan", "Stephan"],
  'Last Name': ["Ivanov", "Petrov", "Dimitrov", "Stoqnov", "Philipov", "Stephanov", "Stephanov"],
  'age': [39, 43, 47, 42, 39, 36, 36],
  'city': ["Sofia", "Sofia", "Plovdiv", "Sofia", "Sofia", "Varna", "Varna"],
  'salary': [1000, 1100, 1000, 1000, 1100, 1000, 1000],
  'grades': [4, 5, 6, 5, 4, 4, 4]
}

dataframeExample = pd.DataFrame(datasetExample, index = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Duplicate"])

print(dataframeExample)
print()

print(dataframeExample.duplicated())

dataframeExample.drop_duplicates(inplace = True)

print(dataframeExample)
print()
