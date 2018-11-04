#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0058

https://projecteuler.net/problem=58

Spiral primes

Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below 10%?
"""

import random

PROBLEM = 58
SOLVED = True
SPEED = float('0.349')
TAGS = ['primality', 'miller_rabin']


def miller_rabin(number, witnesses=10):
    """Determines if number is probably prime via Miller-Rabin"""
    # mostly based on the pseudocode provided in
    # https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    if number == 2 or number == 3:
        return True
    elif number == 1 or number % 2 == 0:
        return False

    # now we have an odd number > 3
    # rewrite n-1 as: 2^r * d (where d is odd)
    odd_part = number - 1
    exponent = 0
    while odd_part % 2 == 0:
        odd_part /= 2
        exponent += 1

    # since there are a number of witnesses that are "strong liars", we need to
    # check more than one witness
    for _ in xrange(witnesses):
        # Pick a random witness
        witness = random.randrange(2, number-1)

        # test_result = witness^odd_part mod number
        test_result = pow(witness, odd_part, number)
        if test_result == 1 or test_result == number-1:
            continue

        # while we can square the number and the squared number is not -1
        # mod number
        for _ in xrange(exponent-1):
            # square and mod the number
            test_result = pow(test_result, 2, number)
            if test_result == number - 1:
                # continue witnessloop
                break
        else:
            return False

    # the number passed the tests, it is probably prime
    return True


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    last = 1
    # total_primes = 0
    diagonal_primes = 0
    for side_len in xrange(3, 100000, 2):
        for _ in xrange(0, 4):
            # numbers = range(last+1, last+side_len)
            # print side_len, side, numbers
            last += side_len - 1
            if miller_rabin(last):
                diagonal_primes += 1
        percent = float(diagonal_primes) / (side_len*2 - 1)
        # print side_len, diagonal_primes, '/', side_len*2 - 1, '=', percent
        if int(percent*100) < 10:
            print side_len, diagonal_primes, '/', side_len*2 - 1, '=', percent
            break


if __name__ == '__main__':
    main()
