from scipy.optimize import linprog


print("Змінні: x — кількість стільців, y — кількість столів")
print("Максимізувати P(x, y) = 500x + 800y")
print("Обмеження ресурсів:")
print("2x + 4y <= 120 (деревина)")
print("3x + 2y <= 90 (робочий час)")
print("x >= 0, y >= 0")

result = linprog(
	[-500, -800],
	A_ub=[[2, 4], [3, 2]],
	b_ub=[120, 90],
	bounds=[(0, None), (0, None)],
	method="highs",
)

if not result.success:
	print(f"Не вдалося знайти оптимальний план: {result.message}")

chairs, tables = result.x
maximum_profit = -result.fun
wood_used = 2 * chairs + 4 * tables
work_hours_used = 3 * chairs + 2 * tables
wood_remaining = 120 - wood_used
work_hours_remaining = 90 - work_hours_used

print("\nОптимальний план виробництва:")
print(f"Стільці: {chairs:.2f}")
print(f"Столи: {tables:.2f}")
print(f"Максимальний прибуток: {maximum_profit:.2f} грн")

print("\nВикористання ресурсів:")
print(
	f"Деревина: використано {wood_used:.2f} з 120 м², "
	f"залишок {wood_remaining:.2f}"
)
print(
	f"Робочий час: використано {work_hours_used:.2f} з 90 год, "
	f"залишок {work_hours_remaining:.2f}"
)

if abs(wood_remaining) < 1e-5:
	print("Деревину використано повністю.")
else:
	print("Деревина залишилася невикористаною.")

if abs(work_hours_remaining) < 1e-5:
	print("Робочий час використано повністю.")
else:
	print("Частина робочого часу залишилася невикористаною.")
