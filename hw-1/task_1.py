import numpy as np

M = np.array([[100, 150, 200], [50, 100, 150], [0, 50, 100]])
E = np.array([[20, 30, 40], [10, 20, 30], [5, 10, 15]])

def update_contrast(N, value):
    return N * value

def update_brightness(N, value):
    return N + value

def apply_blending(N, K, a, b):
    return a * N + b * K

print(update_contrast(M, 0.5))
print(update_brightness(M, 25))
print(apply_blending(M, E, 0.8, 0.2))