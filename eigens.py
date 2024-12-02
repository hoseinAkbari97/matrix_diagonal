import numpy as np

# Define a matrix
A = np.array([[0, 1, 0], [0, 0, 1], [-2, 0, 1]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:")
print(eigenvectors)