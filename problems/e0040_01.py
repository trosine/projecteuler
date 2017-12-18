#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0040

https://projecteuler.net/problem=40

Champernowne's constant

An irrational decimal fraction is created by concatenating the positive
integers:

0.12345678910 1 112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d₁ × d₁₀ × d₁₀₀ × d₁₀₀₀ × d₁₀₀₀₀ × d₁₀₀₀₀₀ × d₁₀₀₀₀₀₀
"""

PROBLEM = 40
SOLVED = True
SPEED = 0.09
TAGS = ['champernowne']


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    maximum = 1e6
    constant = ''
    number = 1
    while len(constant) <= maximum:
        constant += str(number)
        number += 1
    print number
    product = 1
    offset = 1
    while offset <= maximum:
        print offset, constant[offset-1]
        product *= int(constant[offset-1])
        offset *= 10
    print product



if __name__ == '__main__':
    main()
