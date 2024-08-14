import pandas as pd


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

print(dataframeExample)
print()

dataColumnsToRows = pd.melt(dataframeExample)

print(dataColumnsToRows)
print()

datasetExampleConcatRow = {
  'First Name': ["New"],
  'Last Name': ["New"],
  'Age': [0],
  'City': ["New"],
  'Salary': [0],
  'Experience': [0],
  'Grades': [0]
}

dataframeExampleRow = pd.DataFrame(datasetExampleConcatRow)

dataframeExampleConcatRow = pd.concat([dataframeExample, dataframeExampleRow])

print(dataframeExampleConcatRow)
print()

datasetExampleConcatColumn = {
  'New': ["No", "No", "No", "No", "No", "No", "Yes"],
}

dataframeExampleColumn = pd.DataFrame(datasetExampleConcatColumn)

dataframeExampleConcatColumn = pd.concat([dataframeExample, dataframeExampleColumn], axis=1)

print(dataframeExampleConcatColumn)
print()

dataframeExample.sort_values('First Name', ascending=False, inplace=True)

print(dataframeExample)
print()

