import numpy as np

M = np.matrix([[100, 50, 0], [150, 100, 50], [200, 150, 100]])
E = np.matrix([[20, 10, 5], [30, 20, 10], [40, 30, 15]])

def update_contrast(N, value):
    return N * value

def update_brightness(N, value):
    return N + value

def apply_blending(N, K, a, b):
    return a * N + b * K

print(update_contrast(M, 0.5))
print(update_brightness(M, 25))
print(apply_blending(M, E, 0.8, 0.2))