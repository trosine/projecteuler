#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0038

https://projecteuler.net/problem=38

Pandigital multiples

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3).

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2,...,n) where n > 1?
"""

PROBLEM = 38
SOLVED = True
SPEED = 0.05
TAGS = ['pandigital', 'product']
PANDIGITAL = list('123456789')


def pandigital(number):
    """Returns if number is pandigital."""
    return sorted(list(str(number))) == PANDIGITAL

def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    pandigitals = []
    # Since we have to have at least 2 products, the number cannot have more than 4 digits.
    for number in xrange(1, 10000):
        possible = ''
        for multiple in xrange(1, 10):
            possible += str(number * multiple)
            if len(possible) >= 9:
                break
        if pandigital(possible):
            # print number, multiple, possible
            pandigitals.append(possible)
    print 'Max:', max(pandigitals)


if __name__ == '__main__':
    main()
