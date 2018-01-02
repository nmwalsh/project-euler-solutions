"""
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

# Concepts used:
# set, range, union

import math

# question-specific parameters
min_val = 0
max_val = 1000
multiple_one = 3
multiple_two = 5

def sum_of_multiples(min_val, max_val, multiple_one, multiple_two):
	"""
	Function that returns sum of union set of all multiples between min_val and max_val for two given multiples
	"""
	set_one = set(range(min_val, max_val, multiple_one))
	set_two = set(range(min_val, max_val, multiple_two))
	union_sum = sum(set_one | set_two)

	print(union_sum)
	return union_sum

sum_of_multiples(min_val, max_val, multiple_one, multiple_two)