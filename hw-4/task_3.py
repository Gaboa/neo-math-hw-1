from itertools import combinations
from math import prod

failure_probabilities = {
	"A": 0.02,
	"B": 0.05,
	"C": 0.03,
	"D": 0.04,
}

working_probabilities = {
	node: 1 - probability
	for node, probability in failure_probabilities.items()
}

all_working = prod(working_probabilities.values())
at_least_one_failure = 1 - all_working

exactly_two_failures = sum(
	prod(failure_probabilities[node] for node in failed_nodes)
	* prod(
		working_probabilities[node]
		for node in failure_probabilities
		if node not in failed_nodes
	)
	for failed_nodes in combinations(failure_probabilities, 2)
)

print("Імовірність, що всі 4 вузли працюють:")
print(
	"P(усі працюють) = 0.98 * 0.95 * 0.97 * 0.96 = "
	f"{all_working:.6f} ({all_working * 100:.2f}%)"
)

print("\nІмовірність, що відмовить хоча б один вузол:")
print(
	"P(хоча б один відмовить) = 1 - P(усі працюють) = "
	f"{at_least_one_failure:.6f} ({at_least_one_failure * 100:.2f}%)"
)

print("\nІмовірність, що відмовлять рівно 2 вузли:")
print(
	"P(рівно 2 відмови) = сума 6 комбінацій = "
	f"{exactly_two_failures:.6f} ({exactly_two_failures * 100:.2f}%)"
)
