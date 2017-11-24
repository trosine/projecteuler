#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0017

https://projecteuler.net/problem=17

Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE:

Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The
use of "and" when writing out numbers is in compliance with British usage.
"""

PROBLEM = 17
SOLVED = True
SPEED = 0.02
TAGS = ['numbers_to_words']

WORDS = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    1000: 'onethousand',
    }

def get_words(number):
    """Returns a list of words that describe number"""
    words = []
    hundreds = 0
    if number >= 1000:
        thousands = number / 1000
        number %= 1000
        words += get_words(thousands) + ['thousand']
    if number >= 100:
        hundreds = number / 100
        number %= 100
        words += [(WORDS[hundreds]), 'hundred']
        if number:
            words.append('and')
    if not number:
        pass
    elif number > 0 and number < 20:
        # these are exact
        words.append(WORDS[number])
    else:
        tens = number / 10
        number %= 10
        words.append(WORDS[tens * 10])
        if number:
            words.append(WORDS[number])
    return words


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    total = 0
    for num in xrange(1, 1001):
        words = get_words(num)
        # print num, ' '.join(words)
        letters = sum(map(len, words))
        total += letters
        # print '%4d %3d %s' %(num, letters, ' '.join(words))
    print total


if __name__ == '__main__':
    main()
