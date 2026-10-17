import numpy as np
from scipy.integrate import quad
from scipy.optimize import approx_fprime, minimize, minimize_scalar


def productivity(time):
	return 100 + 40 * time - 4 * time**2


def negative_productivity(time):
	return -productivity(time)


def unit_cost(parameters):
	x, y = parameters
	return x**2 + y**2 - 10 * x - 8 * y + 50


def unit_cost_gradient(parameters):
	x, y = parameters
	return [2 * x - 10, 2 * y - 8]


print("Частина перша. Дослідження продуктивності")
print("P(t) = 100 + 40t - 4t^2, 0 <= t <= 10")

for time in (2, 5, 8):
	derivative = approx_fprime(
		np.array([time]),
		lambda value: productivity(value[0]),
		epsilon=1e-6,
	)[0]
	if derivative > 1e-3:
		trend = "продуктивність зростає"
	elif derivative < -1e-3:
		trend = "продуктивність спадає"
	else:
		trend = "продуктивність близька до пікової (похідна ≈ 0)"
	print(f"P'({time}) ≈ {derivative:.6f}: {trend}")

peak_result = minimize_scalar(
	negative_productivity,
	bounds=(0, 10),
	method="bounded",
)
if not peak_result.success:
	print(f"Не вдалося знайти пік продуктивності: {peak_result.message}")

peak_time = peak_result.x
peak_productivity = productivity(peak_time)
total_production, integration_error = quad(productivity, 0, 10)

print(f"Пікова продуктивність: t* = {peak_time:.4f} год")
print(f"P(t*) = {peak_productivity:.4f} одиниць/год")
print(f"Загальний обсяг за зміну: {total_production:.4f} одиниць")

print("\nЧастина друга. Оптимізація витрат")
budget_matrix = np.array([[2, 1], [1, 3]])
budget_values = np.array([20, 25])
initial_parameters = np.linalg.solve(budget_matrix, budget_values)
print(
	f"Розв'язок системи 2x + y = 20, x + 3y = 25: "
	f"(x0, y0) = ({initial_parameters[0]:.4f}, {initial_parameters[1]:.4f})"
)

cost_result = minimize(
	unit_cost,
	initial_parameters,
	method="BFGS",
	jac=unit_cost_gradient,
)
if not cost_result.success:
	print(f"Не вдалося мінімізувати собівартість: {cost_result.message}")

optimal_x, optimal_y = cost_result.x
minimum_unit_cost = cost_result.fun
total_cost = total_production * minimum_unit_cost

print(f"Оптимальні параметри: (x*, y*) = ({optimal_x:.4f}, {optimal_y:.4f})")
print(f"Мінімальна собівартість одиниці: {minimum_unit_cost:.4f}")
print(f"Загальна вартість виробництва за зміну: {total_cost:.2f}")
