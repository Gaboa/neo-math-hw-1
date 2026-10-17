from math import comb

total_batteries = 12
working_batteries = 8
defective_batteries = 4
sample_size = 3

all_working_multiplication = (
	working_batteries / total_batteries
	* (working_batteries - 1) / (total_batteries - 1)
	* (working_batteries - 2) / (total_batteries - 2)
)

all_working_combinatorics = (
	comb(working_batteries, sample_size) / comb(total_batteries, sample_size)
)

exactly_two_working_multiplication = (
	working_batteries / total_batteries
	* (working_batteries - 1) / (total_batteries - 1)
	* defective_batteries / (total_batteries - 2)
	+ working_batteries / total_batteries
	* defective_batteries / (total_batteries - 1)
	* (working_batteries - 1) / (total_batteries - 2)
	+ defective_batteries / total_batteries
	* working_batteries / (total_batteries - 1)
	* (working_batteries - 1) / (total_batteries - 2)
)

exactly_two_working_combinatorics = (
	comb(working_batteries, 2)
	* comb(defective_batteries, 1)
	/ comb(total_batteries, sample_size)
)

print("Правило множення:")
print(
	"P(3 справні) = 8/12 * 7/11 * 6/10 = "
	f"{all_working_multiplication:.6f} ({all_working_multiplication * 100:.2f}%)"
)

print("\nКомбінаторний метод:")
print(
	"P(3 справні) = C(8, 3) / C(12, 3) = "
	f"{all_working_combinatorics:.6f} ({all_working_combinatorics * 100:.2f}%)"
)
print(
	"Результати збігаються: "
	f"{all_working_multiplication == all_working_combinatorics}"
)

print("\nРівно 2 справні батареї:")
print(
	"Правило множення: P(ССД) + P(СДС) + P(ДСС) = "
	f"{exactly_two_working_multiplication:.6f} "
	f"({exactly_two_working_multiplication * 100:.2f}%)"
)
print(
	"Комбінаторний метод: C(8, 2) * C(4, 1) / C(12, 3) = "
	f"{exactly_two_working_combinatorics:.6f} "
	f"({exactly_two_working_combinatorics * 100:.2f}%)"
)
