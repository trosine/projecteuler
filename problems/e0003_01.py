#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0003

https://projecteuler.net/problem=3

Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math
import sys

PROBLEM = 3
SOLVED = True
SPEED = 0.02
TAGS = ['prime', 'factor', 'iterator']


class Primes(object):
    """Iteratable class that handles prime number generation and testing"""

    # cache of currently known primes
    known_primes = [2, 3]

    def __init__(self, maximum=float('inf'), count=float('inf')):
        self.maximum = maximum
        self.count = count
        self.__iter = 0

    def __iter__(self):
        return self

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Cannot use "%s" as a list index' % type(key))
        while len(self.known_primes) <= key:
            self.next()
        return self.known_primes[key]

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
            # print 'Checking to see if candidate %d is prime' % candidate
            if candidate > self.maximum:
                raise StopIteration()
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
            # print 'Checking to see if %d is a factor of %d' % (prime, number)
            if prime == number:
                factors.append(prime)
                break
            # reduce the total iterations
            if prime > math.sqrt(number):
                factors.append(number)
                break
            while not number % prime:
                number /= prime
                factors.append(prime)
                # case for squares (which are divisible)
                if prime == number:
                    factors.append(prime)
                    break
        return factors


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    number = 600851475143
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    factors = Primes.factor(number)
    print factors[-1]


if __name__ == '__main__':
    main()
