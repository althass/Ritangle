from itertools import product, combinations

# Function to check if three values can form a triangle
def can_form_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Generate all possible outcomes of five rolls of a six-sided die
possible_outcomes = list(product(range(1, 7), repeat=5))

# Count of outcomes where no triangle can be formed
no_triangle_count = 0

# Check each outcome
for outcome in possible_outcomes:
    found_triangle = False

    # Check all combinations of three values in the outcome to see if any can form a triangle
    for a, b, c in combinations(outcome, 3):
        if can_form_triangle(a, b, c):
            found_triangle = True
            break

    # If no combination of three values forms a triangle, increment the count
    if not found_triangle:
        no_triangle_count += 1

# Calculate probability
total_outcomes = len(possible_outcomes)
probability_no_triangle = no_triangle_count / total_outcomes
print((probability_no_triangle,))

