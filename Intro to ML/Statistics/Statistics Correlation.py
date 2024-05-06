import matplotlib.pyplot as plt
import pandas as pd



negative_corr = {'a': [19, 23, 34, 35, 38, 55, 61, 79, 99, 100], "b":  [1, 23, 34, 49, 55, 77, 78, 79, 80, 98]}
negative_corr = pd.DataFrame(data=negative_corr)

negative_corr.plot(x = 'a', y = 'b')

plt.show()