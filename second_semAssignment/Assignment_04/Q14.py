import random

# PMF: values and their probabilities
values = [1, 2, 3, 4]
probabilities = [0.1, 0.3, 0.4, 0.2]

# Generate trials
trials = 10000
samples = random.choices(values, weights=probabilities,k=trials)
# print(samples)

# Estimate expected value
expected_value = sum(samples) / trials
print(f"Estimated Expected Value: {expected_value}")
