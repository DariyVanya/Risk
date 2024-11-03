import numpy as np

# Define the payoff matrix F*
F_star = np.array([
    [3, 6, 5, 6],
    [1, 3, 9, 5],
    [4, 3, 5, 7],
    [4, 1, 8, 4]
])

# Define the probability vector P
P = np.array([0.2, 0.3, 0.25, 0.25])

# Step 1: Calculate Bayes Criterion (B* vector)
B_star = F_star.dot(P)

# Step 2: Calculate Modal Criterion (M* vector)
M_star = np.max(F_star, axis=1)

# Step 3: Compromise criterion F*^comp = min(B*, M*)
F_star_comp = np.minimum(B_star, M_star)

# Find the optimal decision by finding the maximum of F_star_comp
optimal_decision_index = np.argmax(F_star_comp)
optimal_decision = optimal_decision_index + 1  # Adding 1 to match indexing in the example

print(B_star, M_star, F_star_comp, "\n", optimal_decision)
