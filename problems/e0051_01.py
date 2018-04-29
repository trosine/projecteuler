#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0051

https://projecteuler.net/problem=51

Prime digit replacements

By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
"""

import itertools
import math

PROBLEM = 51
SOLVED = True
SPEED = float('1.63')
TAGS = ['primes', 'prime_sieve', 'digit_replacement']


def sieve(maximum):
    """Produce a list of primes less than maximum."""
    primes = []
    possible = [True] * maximum
    limit = int(math.sqrt(maximum))
    for candidate in xrange(2, limit):
        if possible[candidate]:
            primes.append(candidate)
            for composite in xrange(candidate**2, maximum, candidate):
                possible[composite] = False
    # every candidate >= sqrt(maximum) is prime
    for candidate in xrange(limit, maximum):
        if possible[candidate]:
            primes.append(candidate)
    return primes


def prime_replacements(base, digits):
    """Find primes generated by replacing digits in base."""
    base_list = list(str(base))
    valid = []
    for replacement in xrange(10):
        if 0 in digits and replacement == 0:
            # cannot start with 0
            continue
        for digit in digits:
            base_list[digit] = str(replacement)
        number = int(''.join(base_list))
        # print number
        if number in PRIMES:
            valid.append(number)
    return valid


def get_bases(length, static_digits):
    """Produce starting bases."""
    minimum = 10 ** (len(static_digits) - 1) + 1
    maximum = 10 ** len(static_digits)
    # this check is necessary, for only having 1 static digit
    # 10**0 + 1 == 1 + 1 == 2
    if minimum == 2:
        minimum = 1
    # only test odds
    for number in xrange(minimum, maximum, 2):
        number = str(number)
        base = ['9'] * length
        # replace the desired static digits in base with digits from number
        for which_replacement in range(0, len(static_digits)):
            base[static_digits[which_replacement]] = number[which_replacement]
        base = int(''.join(base))
        yield base


def get_families(length, minimum=1):
    """Find all families that have 8 members of prime digits."""
    valid_families = []
    all_digits = set(range(length))
    # must replace at least 1 digit, but cannot replace them all
    # replace at least 2: replacing only 1 digit means 3 are divisible by 3
    for number_to_replace in xrange(2, length):
        print 'Replacing %d of %d digits' % (number_to_replace, length)
        combinations = itertools.combinations(all_digits, number_to_replace)
        for replaced_digits in combinations:
            static_digits = all_digits.difference(replaced_digits)
            for base in get_bases(length, list(static_digits)):
                family = prime_replacements(base, replaced_digits)
                if len(family) >= minimum:
                    print base, replaced_digits, family
                    valid_families.append(family)
    return valid_families


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    # print prime_replacements(13, (0,))
    # print prime_replacements(56003, (2,3))
    smallest = None
    for length in xrange(5, 7):
        families = get_families(length, minimum=8)
        for family in sorted(families):
            smallest = family[0]
            break
        if smallest:
            break
    print 'Answer: %d' % (smallest, )


if __name__ == '__main__':
    PRIMES = set(sieve(1000000))
    main()
