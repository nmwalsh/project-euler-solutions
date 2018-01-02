"""
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

# Concepts used:
# set, range, union

import math

min_val = 0
max_val = 1000

fives_set = set(range(min_val, max_val, 5))
threes_set = set(range(min_val, max_val, 3))

union_sum = sum(fives_set | threes_set)

print(union_sum)