from math import sqrt

from scipy.stats import t

sample_mean = 76.8
sample_standard_deviation = 14.2
sample_size = 35
population_mean = 72
alpha = 0.05
degrees_of_freedom = sample_size - 1

standard_error = sample_standard_deviation / sqrt(sample_size)
t_statistic = (sample_mean - population_mean) / standard_error
p_value = 2 * (1 - t.cdf(abs(t_statistic), df=degrees_of_freedom))
critical_t = t.ppf(1 - alpha / 2, df=degrees_of_freedom)
confidence_interval_lower = sample_mean - critical_t * standard_error
confidence_interval_upper = sample_mean + critical_t * standard_error

print("Нульова гіпотеза H0: μ = 72")
print("Альтернативна гіпотеза H1: μ ≠ 72")
print(f"Стандартна похибка середнього SE: {standard_error:.4f}")
print(f"t-статистика: {t_statistic:.4f}")
print(f"p-value двостороннього тесту: {p_value:.4f}")
print(
	"95% довірчий інтервал для середнього: "
	f"[{confidence_interval_lower:.4f}, {confidence_interval_upper:.4f}]"
)

if p_value < alpha:
	print(
		"Висновок: відхиляємо H0. Є статистично значущі підстави вважати, що методика вплинула на результати."
	)
else:
	print(
		"Висновок: не відхиляємо H0. Недостатньо статистичних підстав стверджувати, що методика вплинула на результати."
	)
