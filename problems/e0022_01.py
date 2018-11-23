#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0022

https://projecteuler.net/problem=22

Names scores

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical
value for each name, multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import euler

PROBLEM = 22
SOLVED = True
SPEED = 0.03
TAGS = ['alphabetic_value']


def load_data():
    """Returns the parsed dataset from filename."""
    data = None
    with euler.Resource('names.txt') as infile:
        data = infile.readline()
    data = data.strip('"').split('","')
    data.sort()
    return data


def alphabetic_value(name):
    """Returns the sum of all characters in name with A==1"""
    return sum([ord(x) - 64 for x in name])


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM

    total = 0
    names = load_data()
    for index in xrange(0, len(names)):
        total += (index+1) * alphabetic_value(names[index])
    print total


if __name__ == '__main__':
    main()
