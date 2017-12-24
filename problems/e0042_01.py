#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0042

https://projecteuler.net/problem=42

Coded triangle numbers

The n-th term of the sequence of triangle numbers is given by,

t(n) = n(n+1)/2; so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t(10). If the word value
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
"""

PROBLEM = 42
SOLVED = True
SPEED = 0.03
TAGS = ['triangle_numbers', 'triangle_words']


def load_data(filename):
    """Parse the words from filename."""
    data = None
    with open(filename) as infile:
        data = infile.readline()
    data = data.strip('"').split('","')
    return data


def word_value(word):
    """Calculate the sum of the characters in word."""
    return sum([ord(x) - ord('A') + 1 for x in word])


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    triangles = {}
    for number in range(1, 1000):
        triangle = number * (number+1) / 2
        triangles[triangle] = True
    words = load_data('fixtures/d%04d.txt' % PROBLEM)
    total = 0
    for word in words:
        value = word_value(word)
        if triangles.get(value, False):
            total += 1
    print total


if __name__ == '__main__':
    main()
