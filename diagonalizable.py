import numpy as np

def is_diagonalizable(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return np.linalg.matrix_rank(eigenvectors) == matrix.shape[0]

# Example matrix
A = np.array([[-9, 1, 0], [-26, 0, 1], [-24, 0, 0]])
print(f"Is A diagonalizable? {is_diagonalizable(A)}")