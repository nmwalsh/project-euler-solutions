"""
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

"""
3 functions:
1) sieve: Given a limit, generate list of prime numbers
2) find_max_factor: Given a limit and set of values, find max factor from the array
3) max_prime_factor: Given a limit, efficiently find the maximum prime factor
"""

import math

prompt_val = 600851475143

# Generate list of primes up to a limit
def sieve(limit):
  """
  Sieve of Eratosthenes prime generation algorithm
  - generates identity array from 1 to N
  - Iterates from index 2 up to removes all larger numbers for which current index is a factor
  - Results in list of primes for n(log(log(n))) runtime
  """

  bools = []
  primes = []
  
  # generate a list of booleans all set to True initially
  # the list is indexed from 2 to limit representing all numbers
  # e.g. [True, True, True, True] = [2, 3, 4, 5]
  for i in range(1, limit):
    bools.append(True)
    
  # loop from 2 to limit setting the composite numbers to False
  # we start from 2 because we know 1 is not a prime number
  for i in range(2, limit):
    if bools[i-2]:
      for j in range(i*2, limit+1, i):
        bools[j-2] = False
        
  # now generate the list of primes only where
  # there is a True value in the bools list
  for p in range(0, len(bools)):
    if (bools[p]):
      primes.append(p+2)
  #print(primes)
  return primes

# For a given set and value, find the highest factor from the set.
def find_max_factor(values, limit):
  # Invert ascending values array to descending
  for k in values[::-1]:
  	# If limit / currentval has 0 remainder, return currentval
  	if not limit % k:
  		return k

# Find the maximum prime factor of a given number
def max_prime_factor(limit):
	# We know the largest prime factor must be equal or less than the sqrt
	theoretical_max = math.floor(prompt_val**0.5)
	max_factor = find_max_factor(sieve(theoretical_max), limit)
	print(max_factor)
	return max_factor

max_prime_factor(prompt_val)	 
