import numpy as np

# y = kx + b
t = np.array([1, 2, 3, 4, 5])
y = np.array([22, 28, 37, 45, 53])

A = np.column_stack((t, np.ones(len(t))))

# A.T * A * x = A.T * y
A_T = A.T
A_T_dot_A = A_T @ A
A_T_dot_y = A_T @ y
k_1, b_1 = np.linalg.solve(A_T_dot_A, A_T_dot_y)

k, b = np.linalg.lstsq(A, y, rcond=None)[0]
print(f"k = {k}, b = {b}")
print(f"k_1 = {k_1}, b_1 = {b_1}")
predicted_y = np.dot(A, [k, b])
print("Predicted y:", predicted_y)
print("Check coefficients:", np.allclose([k, b], [k_1, b_1]))

next_y = k * 6 + b
print("Next y:", next_y)