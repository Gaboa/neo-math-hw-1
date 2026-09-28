import math

import numpy as np
from scipy.optimize import approx_fprime


def active_sessions(t):
	return 1000 * t * math.exp(-0.2 * t)


def analytical_derivative(t):
	# f'(t) = 1000 * (1 - 0.2t) * e^(-0.2t)
	return 1000 * math.exp(-0.2 * t) * (1 - 0.2 * t)


def format_time(hours_from_start):
	total_minutes = round((8 + hours_from_start) * 60)
	return f"{total_minutes // 60:02d}:{total_minutes % 60:02d}"

# 1 - 0.2t = 0
peak_time = 5
moments = [2, 6, 10]

print(f"Час піку: {format_time(peak_time)}")
print(f"Кількість активних сесій у цей момент: {active_sessions(peak_time):.2f}")

print("\nЧисельна та аналітична похідні:")

for t in moments:
    gradient = approx_fprime(
        np.array([t], dtype=float),
        lambda value: active_sessions(float(value[0])),
        10 ** -5,
    )
    numerical = float(np.asarray(gradient).flat[0])

    analytical = analytical_derivative(t)
    print(
        f"{format_time(t)} (t={t}): "
        f"чисельна = {numerical:.6f}, "
        f"аналітична = {analytical:.6f}, "
        f"різниця = {abs(numerical - analytical):.6e}"
    )

print("\nБізнес-інтерпретація:")
print("О 10:00 похідна додатна: кількість активних сесій зростає => потрібно більше серверів")
print("О 18:00 похідна від'ємна: активність зменшується => можна зменшувати кількість серверів")
print(f"Максимальну кількість серверів варто мати в роботі близько {format_time(peak_time)}")
