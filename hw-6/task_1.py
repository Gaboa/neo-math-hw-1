from scipy.optimize import minimize_scalar


def profit(price):
	return (price - 800) * (2000 - 0.8 * price)


def negative_profit(price):
	return -profit(price)


price_coefficient = -0.8
linear_coefficient = 2640
analytic_price = -linear_coefficient / (2 * price_coefficient)
second_derivative = 2 * price_coefficient
analytic_max_profit = profit(analytic_price)

result = minimize_scalar(
	negative_profit,
	bounds=(800, 2500),
	method="bounded",
)
numerical_price = result.x
numerical_max_profit = -result.fun

print("Аналітичне розв'язання:")
print("P(x) = -0.8x^2 + 2640x - 1600000")
print("P'(x) = -1.6x + 2640")
print(f"P'(x) = 0 => x* = {analytic_price:.2f}")
print(f"P''(x) = {second_derivative:.1f} < 0, отже це максимум")
print(f"Максимальний місячний прибуток: {analytic_max_profit:.2f}")

print("\nЧисельний пошук:")
print(f"Оптимальна ціна: {numerical_price:.2f}")
print(f"Місячний прибуток: {numerical_max_profit:.2f}")
print(f"Різниця цін з аналітичним результатом: {abs(numerical_price - analytic_price):.6f} грн")
