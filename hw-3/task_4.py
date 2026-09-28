import numpy as np
from scipy.optimize import approx_fprime


def function(point):
	x, y = point
	return 0.5 * x ** 2 + 0.3 * y ** 2 + 0.2 * x * y + 10 * x + 5 * y

# dx => df/dx = x + 0.2y + 10
# dy => df/dy = 0.6 * y + 0.2 * x + 5
def analytical_gradient(point):
	x, y = point
	return np.array([
		x + 0.2 * y + 10,
		0.6 * y + 0.2 * x + 5,
	])


point = np.array([10.0, 20.0])
delta = np.array([0.5, -0.3])

numerical_gradient = approx_fprime(point, function, 10 ** -5)
gradient = analytical_gradient(point)

linear_change = gradient @ delta
exact_change = function(point + delta) - function(point)

print("Аналітичні частинні похідні:")
print("df/dx = x + 0.2y + 10")
print("df/dy = 0.6y + 0.2x + 5")

print(f"\nТочка: (x, y) = ({point[0]:.0f}, {point[1]:.0f})")
print(f"Аналітичний градієнт: ({gradient[0]:.6f}, {gradient[1]:.6f})")
print(f"Чисельний градієнт: ({numerical_gradient[0]:.6f}, {numerical_gradient[1]:.6f})")
print(
	"Різниця компонент: "
	f"({abs(gradient[0] - numerical_gradient[0]):.2e}, "
	f"{abs(gradient[1] - numerical_gradient[1]):.2e})"
)

print("\nЗміна функції при Δx = 0.5, Δy = -0.3:")
print(f"Наближена зміна за лінійною апроксимацією: {linear_change:.6f}")
print(f"Точна зміна f(10.5, 19.7) - f(10, 20): {exact_change:.6f}")
print(f"Різниця між змінами: {abs(linear_change - exact_change):.6f}")
