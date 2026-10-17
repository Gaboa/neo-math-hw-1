def bayes_source(prior_probs, conversion_rates):
	purchase_probability = sum(
		prior * conversion
		for prior, conversion in zip(prior_probs, conversion_rates)
	)

	return [
		prior * conversion / purchase_probability
		for prior, conversion in zip(prior_probs, conversion_rates)
	]


sources = ["Пошукова реклама", "Соцмережі", "Email-розсилка"]
prior_probs = [0.5, 0.3, 0.2]
conversion_rates = [0.04, 0.02, 0.08]

purchase_prob = sum(
	prior * conversion
	for prior, conversion in zip(prior_probs, conversion_rates)
)
post_probs = bayes_source(prior_probs, conversion_rates)

print(f"1. Загальна ймовірність покупки: {purchase_prob * 100:.2f}%")
print(f"\n2. Ймовірність email-розсилки за умови покупки: {post_probs[2] * 100:.2f}%")
print("\n3. Ймовірності джерел після покупки:")
for source, prob in zip(sources, post_probs):
	print(f"{source}: {prob * 100:.2f}%")
