import numpy as np
import pandas as pd

matrix_one = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]

print(matrix_one)

matrix_two = np.array([ [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9] ])
print(matrix_two)


matrix_three = pd.DataFrame([ [1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9] ])
print(matrix_three)