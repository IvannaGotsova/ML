from numpy import random

elementRandom = random.choice([32, 58, 76, 91], p=[0.2, 0.3, 0.5, 0.0], size=(5, 10))

print(elementRandom)
