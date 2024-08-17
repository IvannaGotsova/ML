import pandas as pd
import numpy as np
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

dataframeExamplePromotion = ["No", "Yes", "Yes", "Yes", "No", "No"]

print(dataframeExample)