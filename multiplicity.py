import numpy as np

def algebraic_multiplicity(matrix, eigenvalue):
    char_poly = np.poly(matrix)
    roots = np.roots(char_poly)
    return np.sum(np.isclose(roots, eigenvalue))

def geometric_multiplicity(matrix, eigenvalue):
    eigenspace = null_space(matrix - eigenvalue * np.eye(matrix.shape[0]))
    return eigenspace.shape[1]

def null_space(A):
    u, s, vh = np.linalg.svd(A)
    return vh[np.sum(s > 1e-10):].T

# Example matrix
A = np.array([[0, 1, 0], [0, 0, 1], [-2, 0, 1]])
eigenvalue = 3

print(f"Algebraic multiplicity: {algebraic_multiplicity(A, eigenvalue)}")
print(f"Geometric multiplicity: {geometric_multiplicity(A, eigenvalue)}")