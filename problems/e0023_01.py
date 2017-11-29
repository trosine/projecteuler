#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0023

https://projecteuler.net/problem=23

Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""

import itertools
import math

PROBLEM = 23
SOLVED = True
SPEED = 0.98
TAGS = ['abundant', 'prime', 'prime_sieve', 'prime_factor']


class Primes(object):
    """Iteratable class that handles prime number generation and testing"""

    # cache of currently known primes
    known_primes = [2, 3]

    def __init__(self, maximum=None, count=None, sieve=None):
        self.maximum = float('inf')
        self.count = float('inf')
        self.__iter = 0
        if maximum:
            self.maximum = maximum
            sieve = maximum
        if count:
            self.count = count
        if sieve:
            sieve = int(sieve)
            if sieve > self.known_primes[-1]:
                # only re-initialize if we need more
                self.sieve(sieve)

    def __iter__(self):
        return self

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Cannot use "%s" as a list index' % type(key))
        while len(self.known_primes) <= key:
            self.next()
        return self.known_primes[key]

    @classmethod
    def sieve(cls, maximum):
        """Initialize the known list of primes using Eratosthene sieve
        methodology
        """
        cls.known_primes = []
        possible = [True] * maximum
        limit = int(math.sqrt(maximum))
        for candidate in xrange(2, limit):
            if possible[candidate]:
                cls.known_primes.append(candidate)
                # using candidate**2 as start, because all prior have already
                # been marked as False
                # for example, when marking composites of 3, 6 is already marked
                # composites of 5: 10(2), 15(3), 20(2) are already marked
                for composite in xrange(candidate**2, maximum, candidate):
                    possible[composite] = False
        # every candidate >= sqrt(maximum) is prime
        for candidate in xrange(limit, maximum):
            if possible[candidate]:
                cls.known_primes.append(candidate)

    def next(self):
        """Fetch the next prime number"""
        if self.__iter >= self.count:
            # print 'Reached maximum count %d (%d)' % (self.count, self.__iter)
            raise StopIteration()
        if self.__iter < len(self.known_primes):
            if self.known_primes[self.__iter] > self.maximum:
                raise StopIteration()
            key = self.__iter
            self.__iter += 1
            return self.known_primes[key]
        candidate = self.known_primes[-1] + 2
        while True:
            if candidate > self.maximum:
                raise StopIteration()
            # print 'Checking to see if candidate %d is prime' % candidate
            if not self.first_factor(candidate):
                self.known_primes.append(candidate)
                self.__iter += 1
                return candidate
            candidate += 2

    @classmethod
    def first_factor(cls, number):
        """Returns the lowest factor of the number.
        If the number is prime, None is returned instead.
        """
        for prime in cls(maximum=math.sqrt(number)):
            if not number % prime:
                return prime
        return None

    @classmethod
    def factor(cls, number):
        """Returns a list of prime factors that this number is composed of"""
        factors = []
        for prime in cls():
            if prime > number:
                break
            # print 'Checking to see if %d is a factor of %d' % (prime, number)
            # reduce the total iterations
            if prime > math.sqrt(number):
                factors.append(number)
                break
            while not number % prime:
                number /= prime
                factors.append(prime)
        return factors


# From: https://math.stackexchange.com/questions/22721/is-there-a-formula-to-calculate-the-sum-of-all-proper-divisors-of-a-number
def sum_of_factors(number, proper=True):
    """Returns the sum of all factors for number. If proper=False, includes
    number in the sum.
    """
    divisor_sum = 1
    for prime, group in itertools.groupby(Primes.factor(number)):
        exponent = len(list(group))
        divisor_sum *= (prime ** (exponent + 1) - 1) / (prime - 1)
    if proper:
        divisor_sum -= number
    return divisor_sum


# by the description, 1..23 cannot be written as the sum of 2 abundant numbers
# the upper bound is 28123
def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM

    # This probably only needs to be 28100, but this ensures that we
    # don't fall back to trial division to find the next prime.
    Primes.sieve(29000)

    # first determine the abundant numbers
    # brief analysis also shows odd numbers can only abundant if divisible by 5
    abundant_lookup = [False] * (28123 - 12)
    abundant_numbers = []
    for number in xrange(12, 28123-12):
        if sum_of_factors(number) > number:
            abundant_lookup[number] = True
            abundant_numbers.append(number)
            # print number

    print len(abundant_numbers)
    total = 0
    # now, calculate which ones cannot be created with the sum of 2 abundant numbers
    # technically, we could skip the first 23, but they should be pretty quick
    for number in xrange(1, 28123-12):
        abundant_sum = False
        for candidate in abundant_numbers:
            if candidate > number / 2:
                break
            if abundant_lookup[number - candidate]:
                abundant_sum = True
                # print '%d = %d + %d' % (number, candidate, number-candidate)
                break
        if not abundant_sum:
            total += number

    print total



if __name__ == '__main__':
    main()
