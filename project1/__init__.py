#!/usr/local/bin/python

"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.  Find the sum of all the
multiples of 3 or 5 below 1000.
"""

import argparse

def partial_sum(multiple, maxvalue):
    """Calculates the n-th partial sum of simple arithmatic series where
    f(i) == ni
    """
    how_many = maxvalue / multiple
    return how_many * (multiple + multiple * how_many) / 2

def calculate(maxvalue):
    """Calculate the sum of all multiples of 3 and 5 below maxvalue quickly"""
    sum3 = partial_sum(3, maxvalue-1)
    sum5 = partial_sum(5, maxvalue-1)
    sum15 = partial_sum(15, maxvalue-1)
    print sum3 + sum5 - sum15

def calculate_brute(maxvalue):
    """Calculate the sum of all multiples of 3 and 5 below maxvalue via brute force"""
    total = 0
    for i in xrange(1, maxvalue):
        if not i % 3 or not i % 5:
            total += i
    print total

def main():
    """Main routine called when run as a script"""
    parser = argparse.ArgumentParser()
    parser.add_argument('max', type=int)
    args = parser.parse_args()

    calculate(args.max)

if __name__ == '__main__':
    main()
