import pandas as pd

datasetExample = {
  'First Name': ["Ivan", "Petar", "Dimitar", "Stoqn", "Philip", "Stephan", " ", 1 , ' '],
  'Last Name': ["Ivanov", "Petrov", "Dimitrov", "Stoqnov", "Philipov", "Stephanov", 2, 2, 2],
  'age': [39, 43, 47, 42, 39, 36, "", "", ""],
  'city': ["Sofia", "Sofia", "Plovdiv", "Sofia", "Sofia", "Varna", 'null', 'null', 'null'],
  'salary': [1000, 1100, 1000, 1000, 1100, 1000, 'null', 'null', 'null'],
  'grades': [4, 5, 6, 5, 4, 4, 'null', 'null', 'null']
}

dataframeExample = pd.DataFrame(datasetExample, index = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "WrongOne", "WrongTwo", "WrongThree"])

print(dataframeExample)
print()

dataframeExampleEmpty = dataframeExample.dropna()
print(dataframeExampleEmpty)