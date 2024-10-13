import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

data = [
    ['1', ['Bread', 'Milk', 'Vegetables', 'Salad']],
    ['2', ['Milk', 'Fruits', 'Cheese', 'Fruits', 'Eggs', 'Juice']],
    ['3', ['Milk', 'Salad', 'Cheese']],
    ['4', ['Bread', 'Milk', 'Fruits', 'Eggs', 'Cheese', 'Vegetables']],
    ['5', ['Bread', 'Salad', 'Eggs', 'Milk', 'Salad', 'Vegetables']],
    ['6', ['Milk', 'Salad', 'Bread', 'Cheese', 'Vegetables', 'Eggs', 'Ice Cream']],
    ['7', ['Bread', 'Salad', 'Eggs', 'Milk']],
    ['8', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['9', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['10', ['Bread', 'Milk', 'Vegetables', 'Salad', 'Eggs']],
    ['11', ['Milk', 'Fruits', 'Salad', 'Eggs']],
    ['12', ['Milk', 'Salad', 'Cheese', 'Vegetables', 'Eggs', 'Milk']],
    ['13', ['Bread', 'Milk', 'Fruits']],
    ['14', ['Bread', 'Salad', 'Ice Cream', 'Milk', 'Vegetables']],
    ['15', ['Milk', 'Salad', 'Fruits', 'Cheese', 'Fruits']],
    ['16', ['Bread', 'Salad', 'Fruits', 'Milk', 'Juice']],
    ['17', ['Bread', 'Milk', 'Salad', 'Vegetables', 'Eggs', 'Cheese', 'Vegetables']],
    ['18', ['Bread', 'Milk', 'Salad', 'Eggs', 'Cheese']],
    ['Я9', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['20', ['Bread', 'Milk', 'Salad', 'Vegetables']]
]

