#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0027

https://projecteuler.net/problem=27

Quadratic primes

Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive
integer values 0 ≤ n ≤ 39. However, when n = 40, 40² + 40 + 41 = 40(40 + 1) +
41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly
divisible by 41.

The incredible formula n² - 79n + 1601 was discovered, which produces 80 primes
for the consecutive values 0 ≤ n ≤ 79. The product of the coefficients, −79 and
1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| ≤ 1000

where |n| is the modulus/absolute value of n

e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
"""

import itertools
import math

PROBLEM = 27
SOLVED = True
SPEED = 4.77
TAGS = ['primes', 'quadratic_primes', 'quadratic']


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


def quadratic_primes(a, b):
    """Returns the number of consecutive primes for n² + an + b
    starting from n=0.
    """
    # pylint: disable=locally-disabled, invalid-name
    # since n starts from 0, it doubles as a counter
    n = 0
    while n*n + a*n + b in Primes.known_primes:
        n += 1
    return n

def main():
    """Solve problem."""
    # pylint: disable=locally-disabled, invalid-name
    print 'Project Euler: %04d' % PROBLEM
    # assume that our answer will result in fewer primes than n² - 79n + 1601
    # which produces the maximum prime of 1601
    Primes.sieve(1602)
    print 'Primes known:', len(Primes.known_primes)
    cap = 1000
    maximum = (0, -cap, -cap)
    # While the description of the problem states |b| ≤ 1000, there's no
    # point in testing b < 0, since n=0, would result in a negative number
    for a, b in itertools.product(xrange(-cap+1, cap), xrange(cap+1)):
        if not b % 2:
            # when n=0, the formula == b
            # and there's no sense in testing non-prime values of b
            continue
        count = quadratic_primes(a, b)
        maximum = max(maximum, (count, a, b))
    print 'Count=%d, a=%d, b=%d' % maximum
    print 'Product=%d' % (maximum[1] * maximum[2])


if __name__ == '__main__':
    main()
