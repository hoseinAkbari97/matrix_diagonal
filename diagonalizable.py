import numpy as np

def is_diagonalizable(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return np.linalg.matrix_rank(eigenvectors) == matrix.shape[0]

# Example matrix
A = np.array([[0, 1, 0], [0, 0, 1], [-2, 0, 1]])
print(f"Is A diagonalizable? {is_diagonalizable(A)}")