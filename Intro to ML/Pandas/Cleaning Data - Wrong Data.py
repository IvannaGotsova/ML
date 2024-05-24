import pandas as pd

datasetExample = {
  'First Name': ["Ivan", "Petar", "Dimitar", "Stoqn", "Philip", "Stephan", "Wrong"],
  'Last Name': ["Ivanov", "Petrov", "Dimitrov", "Stoqnov", "Philipov", "Stephanov", "Wrong"],
  'age': [39, 43, 47, 42, 39, 36, 0],
  'city': ["Sofia", "Sofia", "Plovdiv", "Sofia", "Sofia", "Varna", "Wrong"],
  'salary': [1000, 1100, 1000, 1000, 1100, 1000, 0],
  'grades': [4, 5, 90, 5, 4, 4, 0]
}

dataframeExample = pd.DataFrame(datasetExample, index = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Wrong"])

print(dataframeExample)
print()

for x in dataframeExample.index:
  if dataframeExample.loc[x, "grades"] > 6:
    dataframeExample.loc[x, "grades"] = 6

  if dataframeExample.loc[x, "grades"] <= 0:
    dataframeExample.drop(x, inplace = True)

print(dataframeExample)