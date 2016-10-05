"""
Problem:

    The function add_primes takes an integer, n, and should add all 
    the prime numbers less than or equal to n.

    e.g. add_primes(13) = 2 + 3 + 5 + 7 + 11 + 13 = 

Tests:

    >>> add_primes(13)
    41
    >>> add_primes(30)
    129
    >>> add_primes(1500)
    165040

Hint:

    Could use your is_prime function here from the previous problem?

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def add_primes(n):

