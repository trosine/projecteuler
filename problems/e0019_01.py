#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0019

https://projecteuler.net/problem=19

Counting Sundays

You are given the following information, but you may prefer to do some research
for yourself.

* 1 Jan 1900 was a Monday.

* Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.

* A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1
Jan 1901 to 31 Dec 2000)?
"""

PROBLEM = 19
SOLVED = True
SPEED = 0.02
TAGS = ['date', 'leap_years']

MONTH_DAYS = {
    4: 30,   # April
    6: 30,   # June
    9: 30,   # September
    11: 30,  # November
    }


def days_in_month(year, month):
    """Returns the number of days in month/year"""
    if month != 2:
        return MONTH_DAYS.get(month, 31)
    if not year % 400:
        return 29
    if not year % 100:
        return 28
    if not year % 4:
        return 29
    return 28


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    # 1 Jan 1900 was Monday (1), add 1 year (365), modulate to proper day
    day_of_week = (1+365) % 7
    total = 0

    for year in xrange(1901, 2001):
        for month in xrange(1, 13):
            if day_of_week == 0:
                # print '%d-%02d-01 was a sunday' % (year, month)
                total += 1
            day_of_week = (day_of_week + days_in_month(year, month)) % 7
    print total


if __name__ == '__main__':
    main()
