#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0015

https://projecteuler.net/problem=15

Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

import math
import sys

PROBLEM = 15
SOLVED = True
SPEED = 0.02
TAGS = ['combinations']

def choose(objects, picks):
    """Return the number of combinations (nCr)"""
    fact = math.factorial
    return fact(objects) / (fact(picks) * fact(objects-picks))

# This problem simplifies to [(A+B) choose A] where A=20, B=20 (the sides)
# you start with A+B moves, "choose" A of them to be R, the rest are D
# Another accurate explanation is that there are (A+B)! permutations of 'RrDd'
# but since the # different Rs and Ds are really the same, you divide out their
# permutations (Rr == rR) - A!, B!
# the end result is (A+B)!/(A!*B!)
def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    grid = 20
    if len(sys.argv) > 1:
        grid = int(sys.argv[1])
    print choose(grid*2, grid)


if __name__ == '__main__':
    main()
