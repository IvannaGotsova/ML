import numpy as np
import scipy

arrayExample = np.array([0, 1, 0, 2, 1, 1, 0, 0, 0, 2, 0, 0, 1, 0, 2, 1, 1, 0, 0, 0, 2, 0, 0, 0, 1, 1, 2, 0, 1, 1, 0, 1, 1, 0, 0, 20, 0, 0, 2, 0, 0, 0, 1, 1, 2, 0, 1, 1, 0, 1, 1, 0, 0, 20, 0, 1, 1, 2, 0, 1, 1, 0, 1, 1, 0, 0, 2])

print(scipy.sparse.csr_matrix(arrayExample))
print(scipy.sparse.csr_matrix(arrayExample).data)
print(scipy.sparse.csr_matrix(arrayExample).count_nonzero())

newMatrix = scipy.sparse.csr_matrix(arrayExample)
newMatrix.eliminate_zeros()
newMatrix.sum_duplicates()
print(newMatrix.tocsr())