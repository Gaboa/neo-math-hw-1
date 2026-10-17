from scipy.stats import binom

n = 50
p = 0.88

expected_value = binom.mean(n, p)
standard_dev = binom.std(n, p)

all_on_time_prob = binom.pmf(50, n, p)
exactly_45_prob = binom.pmf(45, n, p)
between_42_and_46_prob = binom.cdf(46, n, p) - binom.cdf(41, n, p)
more_than_5_late_prob = binom.cdf(44, n, p)

print(f"Математичне сподівання E[X]: {expected_value:.4f}")
print(f"Стандартне відхилення: {standard_dev:.4f}")
print(f"Ймовірність, що всі 50 замовлень доставлять вчасно: {all_on_time_prob:.6f}")
print(f"Ймовірність рівно 45 вчасних доставок: {exactly_45_prob:.6f}")
print(f"Ймовірність від 42 до 46 вчасних доставок: {between_42_and_46_prob:.6f}")
print(f"Ймовірність, що запізняться більше 5 замовлень: {more_than_5_late_prob:.6f}")
