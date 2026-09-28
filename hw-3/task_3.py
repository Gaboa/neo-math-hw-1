import math

from scipy.integrate import quad


def registration_rate(t):
	return 500 * math.exp(-0.3 * t)


# F(t) = -(500 / 0.3) * e^(-0.3t) + C
def analytical_integral(start, end):
	return (500 / 0.3) * (math.exp(-0.3 * start) - math.exp(-0.3 * end))

# 0 - (-500 / 0.3 * e^(-0.3*0)) = 500 / 0.3
maximum_registrations = 500 / 0.3
first_week_registrations = analytical_integral(0, 7)
numerical_registrations, numerical_error = quad(registration_rate, 0, 7)
first_week_efficiency = first_week_registrations / maximum_registrations * 100

print(f"Аналітична кількість реєстрацій за перші 7 днів: {first_week_registrations:.2f}")
print(f"Чисельна кількість реєстрацій за перші 7 днів: {numerical_registrations:.2f}")
print(f"Похибка чисельного інтегрування: {numerical_error:.2e}")
print(f"Різниця між результатами: {abs(first_week_registrations - numerical_registrations):.2e}")
print(f"Теоретичний максимум реєстрацій: {maximum_registrations:.2f}")
print(f"Ефективність першого тижня: {first_week_efficiency:.2f}%")
