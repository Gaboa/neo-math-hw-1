import numpy as np

A = np.array([[4, 4, 6], [1, 1, 2], [1, 2, 4]])
b = np.array([460, 130, 240])

det_A = np.linalg.det(A)
print(det_A)

if det_A != 0:
    x = np.linalg.solve(A, b)
    print(x)
    print("Check:", np.allclose(A @ x, b))
else:
    print("The matrix A cannot be solved.")