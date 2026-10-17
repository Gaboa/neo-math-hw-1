from scipy.stats import expon

scale = 10

expected_value = expon.mean(scale=scale)
standard_deviation = expon.std(scale=scale)
less_than_5_probability = expon.cdf(5, scale=scale)
more_than_15_probability = expon.sf(15, scale=scale)
between_5_and_15_probability = expon.cdf(15, scale=scale) - expon.cdf(5, scale=scale)
median_time = expon.ppf(0.5, scale=scale)

print(f"Математичне сподівання E[T]: {expected_value:.2f} хвилин")
print(f"Стандартне відхилення σ: {standard_deviation:.2f} хвилин")
print(f"Ймовірність, що замовлення надійде менше ніж за 5 хвилин: {less_than_5_probability:.4f}")
print(f"Ймовірність чекати більше 15 хвилин: {more_than_15_probability:.4f}")
print(f"Ймовірність отримати замовлення між 5 і 15 хвилинами: {between_5_and_15_probability:.4f}")
print(f"Медіанний час очікування: {median_time:.2f} хвилин")
