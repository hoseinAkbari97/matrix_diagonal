import numpy as np

# Example matrix
A = np.array([[0, 1, 0], [0, 0, 1], [-2, 0, 1]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Form the diagonal matrix of eigenvalues
diagonal_matrix = np.diag(eigenvalues)

# Verify decomposition: Reconstruct the original matrix
reconstructed_A = eigenvectors @ diagonal_matrix @ np.linalg.inv(eigenvectors)

# Display results
print("Original Matrix:\n", A)
print("\nEigenvalues:\n", eigenvalues)
print("\nEigenvectors:\n", eigenvectors)
print("\nDiagonal Matrix (Λ):\n", diagonal_matrix)
print("\nReconstructed Matrix:\n", reconstructed_A)
