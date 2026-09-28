from scipy.integrate import solve_ivp

M = 100
r = 0.15

def learning_rate(t, K):
	return r * (M - K)

solution = solve_ivp(
	learning_rate,
	(0, 30),
	[10],
	dense_output=True,
)

print("Модель навчання: dK/dt = r(M - K)")
print(f"M = {M}, r = {r}, K(0) = 10")
print(f"Рівень знань через 30 днів: {solution.y[0, -1]:.2f}%")

def time_to_90_percent(initial_knowledge):
	def reached_90_percent(t, K):
		return K[0] - 90

	reached_90_percent.terminal = True # type: ignore
	reached_90_percent.direction = 1 # type: ignore

	result = solve_ivp(
		learning_rate,
		(0, 30),
		[initial_knowledge],
		events=reached_90_percent,
		rtol=1e-8,
		atol=1e-8,
	)

	return float(result.t_events[0][0])


print("\nЧас досягнення 90% знань:")
for initial_knowledge in (5, 10, 20):
	time = time_to_90_percent(initial_knowledge)
	print(f"K(0) = {initial_knowledge}%: {time:.2f} днів")

print("\nВисновок:")
print("Чим вищий початковий рівень підготовки, тим менше часу потрібно для досягнення 90% знань. Але різниця не є надто великою.")
