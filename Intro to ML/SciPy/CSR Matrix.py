from scipy.sparse import csr_matrix

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [0, 0, 0, 0]]

print(csr_matrix(matrix))
print(csr_matrix(matrix).data)
print(csr_matrix(matrix).count_nonzero())

matrix = csr_matrix(matrix)
matrix.eliminate_zeros()

print(csr_matrix(matrix).tocsc())