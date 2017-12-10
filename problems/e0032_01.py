#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0032

https://projecteuler.net/problem=32

Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""

import math

PROBLEM = 32
SOLVED = True
SPEED = 0.13
TAGS = ['pandigital']
PANDIGITAL = set('123456789')


# there is no way to create 9 digits if the left side contains less than 5 digits:
#   (97*86 = 8342) [8 digits]
#   (9*876 = 7884) [8 digits]
# it is similarly not possible if the left side contains more than 5 digits:
#   (1*10000 = 10000) [11 digits]
#   (10*1000 = 10000) [11 digits]
#   (100*100 = 10000) [11 digits]
# which means the left side must be 5 digits and the product must be 4 digits
def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    products = set()
    for product in xrange(1000, 10000):
        for multiplier in xrange(2, int(math.sqrt(product))+1):
            if not product % multiplier:
                multiplicand = product / multiplier
                if set('%d%d%d' % (multiplicand, multiplier, product)) == PANDIGITAL:
                    products.add(product)
                    print '%d * %d = %d' % (multiplicand, multiplier, product)
    print products
    print sum(products)


if __name__ == '__main__':
    main()
