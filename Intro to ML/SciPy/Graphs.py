import numpy as np
import scipy

arrayExample = np.array([[0, 1, 2, 0, 1, 2], [0, 1, 2, 2, 0, 0], [1, 0, 0, 1, 0, 0], [2, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 0], [2, 0, 0, 2, 0, 0]])

matrixExample = scipy.sparse.csr_matrix(arrayExample)

print(scipy.sparse.csgraph.connected_components(matrixExample))