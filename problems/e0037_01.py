#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0037

https://projecteuler.net/problem=37

Truncatable primes

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import math

PROBLEM = 37
SOLVED = True
SPEED = 0.24
TAGS = ['primes', 'prime_sieve', 'digit_truncation']


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



def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    found = 0
    truncatable = []
    Primes.sieve(1000000)
    primes = set(Primes.known_primes)
    for prime in Primes.known_primes:
        # Skip primes 2, 3, 5, 7 per description
        if prime <= 7:
            continue
        # Remove digits from the right
        truncated = prime / 10
        while truncated:
            if truncated not in primes:
                break
            truncated /= 10
        if truncated:
            continue
        # Remove digits from the left
        modulus = 10 ** int(math.log10(prime))
        truncated = prime % modulus
        while truncated:
            if truncated not in primes:
                break
            modulus /= 10
            truncated %= modulus
        if truncated:
            continue

        found += 1
        print '%2d - truncatable=%d' % (found, prime)
        truncatable.append(prime)
        # According to the description, there are only 11
        if found == 11:
            break
    print 'Found:', found
    print sum(truncatable)


if __name__ == '__main__':
    main()
