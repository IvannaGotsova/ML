import pandas as pd
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
    ['19', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['20', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['21', ['Bread', 'Milk', 'Vegetables', 'Salad']],
    ['22', ['Milk', 'Fruits', 'Cheese', 'Fruits', 'Eggs', 'Juice']],
    ['23', ['Milk', 'Salad', 'Cheese']],
    ['24', ['Bread', 'Milk', 'Fruits', 'Eggs', 'Cheese', 'Vegetables']],
    ['25', ['Bread', 'Salad', 'Eggs', 'Milk', 'Salad', 'Vegetables']],
    ['26', ['Milk', 'Salad', 'Bread', 'Cheese', 'Vegetables', 'Eggs', 'Ice Cream']],
    ['27', ['Bread', 'Salad', 'Eggs', 'Milk']],
    ['28', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['29', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['30', ['Bread', 'Milk', 'Vegetables', 'Salad', 'Eggs']],
    ['31', ['Milk', 'Fruits', 'Salad', 'Eggs']],
    ['32', ['Milk', 'Salad', 'Cheese', 'Vegetables', 'Eggs', 'Milk']],
    ['33', ['Bread', 'Milk', 'Fruits']],
    ['34', ['Bread', 'Salad', 'Ice Cream', 'Milk', 'Vegetables']],
    ['35', ['Milk', 'Salad', 'Fruits', 'Cheese', 'Fruits']],
    ['36', ['Bread', 'Salad', 'Fruits', 'Milk', 'Juice']],
    ['37', ['Bread', 'Milk', 'Salad', 'Vegetables', 'Eggs', 'Cheese', 'Vegetables']],
    ['38', ['Bread', 'Milk', 'Salad', 'Eggs', 'Cheese']],
    ['39', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['40', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['41', ['Bread', 'Milk', 'Vegetables', 'Salad']],
    ['42', ['Milk', 'Fruits', 'Cheese', 'Fruits', 'Eggs', 'Juice']],
    ['43', ['Milk', 'Salad', 'Cheese']],
    ['44', ['Bread', 'Milk', 'Fruits', 'Eggs', 'Cheese', 'Vegetables']],
    ['45', ['Bread', 'Salad', 'Eggs', 'Milk', 'Salad', 'Vegetables']],
    ['46', ['Milk', 'Salad', 'Bread', 'Cheese', 'Vegetables', 'Eggs', 'Ice Cream']],
    ['47', ['Bread', 'Salad', 'Eggs', 'Milk']],
    ['48', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['49', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['50', ['Bread', 'Milk', 'Vegetables', 'Salad', 'Eggs']],
    ['51', ['Milk', 'Fruits', 'Salad', 'Eggs']],
    ['52', ['Milk', 'Salad', 'Cheese', 'Vegetables', 'Eggs', 'Milk']],
    ['53', ['Bread', 'Milk', 'Fruits']],
    ['54', ['Bread', 'Salad', 'Ice Cream', 'Milk', 'Vegetables']],
    ['55', ['Milk', 'Salad', 'Fruits', 'Cheese', 'Fruits']],
    ['56', ['Bread', 'Salad', 'Fruits', 'Milk', 'Juice']],
    ['57', ['Bread', 'Milk', 'Salad', 'Vegetables', 'Eggs', 'Cheese', 'Vegetables']],
    ['58', ['Bread', 'Milk', 'Salad', 'Eggs', 'Cheese']],
    ['59', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['60', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['61', ['Bread', 'Milk', 'Vegetables', 'Salad']],
    ['62', ['Milk', 'Fruits', 'Cheese', 'Fruits', 'Eggs', 'Juice']],
    ['63', ['Milk', 'Salad', 'Cheese']],
    ['64', ['Bread', 'Milk', 'Fruits', 'Eggs', 'Cheese', 'Vegetables']],
    ['65', ['Bread', 'Salad', 'Eggs', 'Milk', 'Salad', 'Vegetables']],
    ['66', ['Milk', 'Salad', 'Bread', 'Cheese', 'Vegetables', 'Eggs', 'Ice Cream']],
    ['67', ['Bread', 'Salad', 'Eggs', 'Milk']],
    ['68', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['69', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['70', ['Bread', 'Milk', 'Vegetables', 'Salad', 'Eggs']],
    ['71', ['Milk', 'Fruits', 'Salad', 'Eggs']],
    ['72', ['Milk', 'Salad', 'Cheese', 'Vegetables', 'Eggs', 'Milk']],
    ['73', ['Bread', 'Milk', 'Fruits']],
    ['74', ['Bread', 'Salad', 'Ice Cream', 'Milk', 'Vegetables']],
    ['75', ['Milk', 'Salad', 'Fruits', 'Cheese', 'Fruits']],
    ['76', ['Bread', 'Salad', 'Fruits', 'Milk', 'Juice']],
    ['77', ['Bread', 'Milk', 'Salad', 'Vegetables', 'Eggs', 'Cheese', 'Vegetables']],
    ['78', ['Bread', 'Milk', 'Salad', 'Eggs', 'Cheese']],
    ['79', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['80', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['81', ['Bread', 'Milk', 'Vegetables', 'Salad']],
    ['82', ['Milk', 'Fruits', 'Cheese', 'Fruits', 'Eggs', 'Juice']],
    ['83', ['Milk', 'Salad', 'Cheese']],
    ['84', ['Bread', 'Milk', 'Fruits', 'Eggs', 'Cheese', 'Vegetables']],
    ['85', ['Bread', 'Salad', 'Eggs', 'Milk', 'Salad', 'Vegetables']],
    ['86', ['Milk', 'Salad', 'Bread', 'Cheese', 'Vegetables', 'Eggs', 'Ice Cream']],
    ['87', ['Bread', 'Salad', 'Eggs', 'Milk']],
    ['88', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['89', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['90', ['Bread', 'Milk', 'Vegetables', 'Salad', 'Eggs']],
    ['91', ['Milk', 'Fruits', 'Salad', 'Eggs']],
    ['92', ['Milk', 'Salad', 'Cheese', 'Vegetables', 'Eggs', 'Milk']],
    ['93', ['Bread', 'Milk', 'Fruits']],
    ['94', ['Bread', 'Salad', 'Ice Cream', 'Milk', 'Vegetables']],
    ['95', ['Milk', 'Salad', 'Fruits', 'Cheese', 'Fruits']],
    ['96', ['Bread', 'Salad', 'Fruits', 'Milk', 'Juice']],
    ['97', ['Bread', 'Milk', 'Salad', 'Vegetables', 'Eggs', 'Cheese', 'Vegetables']],
    ['98', ['Bread', 'Milk', 'Salad', 'Eggs', 'Cheese']],
    ['99', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['100', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['101', ['Bread', 'Milk', 'Vegetables', 'Salad']],
    ['102', ['Milk', 'Fruits', 'Cheese', 'Fruits', 'Eggs', 'Juice']],
    ['103', ['Milk', 'Salad', 'Cheese']],
    ['104', ['Bread', 'Milk', 'Fruits', 'Eggs', 'Cheese', 'Vegetables']],
    ['105', ['Bread', 'Salad', 'Eggs', 'Milk', 'Salad', 'Vegetables']],
    ['106', ['Milk', 'Salad', 'Bread', 'Cheese', 'Vegetables', 'Eggs', 'Ice Cream']],
    ['107', ['Bread', 'Salad', 'Eggs', 'Milk']],
    ['108', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['109', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['110', ['Bread', 'Milk', 'Vegetables', 'Salad', 'Eggs']],
    ['111', ['Milk', 'Fruits', 'Salad', 'Eggs']],
    ['112', ['Milk', 'Salad', 'Cheese', 'Vegetables', 'Eggs', 'Milk']],
    ['113', ['Bread', 'Milk', 'Fruits']],
    ['114', ['Bread', 'Salad', 'Ice Cream', 'Milk', 'Vegetables']],
    ['115', ['Milk', 'Salad', 'Fruits', 'Cheese', 'Fruits']],
    ['116', ['Bread', 'Salad', 'Fruits', 'Milk', 'Juice']],
    ['117', ['Bread', 'Milk', 'Salad', 'Vegetables', 'Eggs', 'Cheese', 'Vegetables']],
    ['118', ['Bread', 'Milk', 'Salad', 'Eggs', 'Cheese']],
    ['119', ['Bread', 'Milk', 'Salad', 'Vegetables']],
    ['120', ['Bread', 'Milk', 'Salad', 'Vegetables']]
]

data_to_used = [item[1] for item in data]


transaction_encoder = TransactionEncoder()
transaction_encoder_data = transaction_encoder.fit(data_to_used).transform(data_to_used)
dataframe = pd.DataFrame(transaction_encoder_data, columns=transaction_encoder.columns_)


frequent_itemsets = apriori(dataframe, min_support=0.5, use_colnames=True)

association_rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)


print()
print("FREQUENT ITEMSETS:")
print(frequent_itemsets)
print()
print()
print()
print("RULES")
print(association_rules)

