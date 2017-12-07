#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0031

https://projecteuler.net/problem=31

Coin sums

In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

import sys

PROBLEM = 31
SOLVED = True
SPEED = 0.03
TAGS = ['denominations', 'coins']


def coin_combinations(target, coins):
    """Calculates the number of combinations that can produce the target given
    the coins with the values contained in coins.
    """
    remainder = coins[1:]
    total = 0
    for subtotal in xrange(0, target+1, coins[0]):
        if len(remainder) > 1:
            total += coin_combinations(target-subtotal, remainder)
        else:
            # only 1p coins left
            total += 1
    return total


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    target = 200
    if len(sys.argv) > 1:
        target = int(sys.argv[1])
    print coin_combinations(target, coins)


if __name__ == '__main__':
    main()
