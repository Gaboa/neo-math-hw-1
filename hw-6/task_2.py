from math import sqrt

from scipy.optimize import minimize


def objective(point):
	x, y = point
	return x**2 + x * y + y**2 - 6 * x - 9 * y + 20


def gradient(point):
	x, y = point
	return [2 * x + y - 6, x + 2 * y - 9]


analytic_x = 1
analytic_y = 4
hessian = [[2, 1], [1, 2]]
value_discriminant = 16 - 12
value_1 = (4 - sqrt(value_discriminant)) / 2
value_2 = (4 + sqrt(value_discriminant)) / 2
analytic_minimum = objective((analytic_x, analytic_y))

print("Аналітичне розв'язання:")
print("df/dx = 2x + y - 6 = 0")
print("df/dy = x + 2y - 9 = 0")
print(f"Критична точка: (x*, y*) = ({analytic_x}, {analytic_y})")
print(f"Матриця Гессе: {hessian}")
print("det(H - λI) = (2 - λ)^2 - 1 = λ^2 - 4λ + 3 = 0")
print(f"Власні значення: λ1 = {value_1:.0f}, λ2 = {value_2:.0f}")
print("Обидва власні значення додатні, тому критична точка є мінімумом.")
print(f"Значення функції в точці мінімуму: f(1, 4) = {analytic_minimum:.2f}")

initial_points = [(0, 0), (10, 10), (-5, 15)]
optimization_results = [
	(initial_point, minimize(objective, initial_point, method="BFGS", jac=gradient))
	for initial_point in initial_points
]

print("\nЧисельна оптимізація методом BFGS:")
for initial_point, result in optimization_results:
	print(
		f"Початкова точка {initial_point}: "
		f"мінімум ({result.x[0]:.6f}, {result.x[1]:.6f}), "
		f"f = {result.fun:.6f}, успіх: {result.success}"
	)

all_converged_to_minimum = all(
	result.success
	and abs(result.x[0] - analytic_x) < 1e-6
	and abs(result.x[1] - analytic_y) < 1e-6
	for _, result in optimization_results
)
if all_converged_to_minimum:
	print("Усі запуски збіглися до аналітичної точки мінімуму (1, 4).")
else:
	print("Не всі запуски збіглися до аналітичної точки мінімуму.")
