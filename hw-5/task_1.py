import numpy as np

ratings = np.array([1, 2, 3, 4, 5])
review_counts = np.array([120, 180, 320, 580, 800])
total_reviews = np.sum(review_counts)

pmf = review_counts / total_reviews
cdf = np.cumsum(pmf)

expected_value = np.sum(ratings * pmf)
expected_square = np.sum(ratings**2 * pmf)
variance = expected_square - expected_value**2
standard_deviation = np.sqrt(variance)

negative_probability = np.sum(pmf[ratings <= 2])
positive_probability = np.sum(pmf[ratings >= 4])
median_rating = ratings[np.argmax(cdf >= 0.5)]

print("Розподіл оцінок:")
print(f"{'Оцінка':>8} {'PMF':>10} {'CDF':>10}")
for rating, probability, cumulative_probability in zip(ratings, pmf, cdf):
	print(f"{rating:>8} {probability:>10.4f} {cumulative_probability:>10.4f}")

print(f"\nМатематичне сподівання E[X]: {expected_value:.4f}")
print(f"Дисперсія Var(X): {variance:.4f}")
print(f"Стандартне відхилення: {standard_deviation:.4f}")
print(f"Ймовірність оцінки 1 або 2 зірки: {negative_probability * 100:.2f}%")
print(f"Ймовірність оцінки 4 або 5 зірок: {positive_probability * 100:.2f}%")
print(f"Медіана рейтингу: {median_rating}")
