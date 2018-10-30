#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0054

https://projecteuler.net/problem=54

Poker hands

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:

2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand    Player 1            Player 2            Winner
1       5H 5C 6S 7S KD      2C 3S 8S 8D TD      Player 2
        Pair of Fives       Pair of Eights
2       5D 8C 9S JS AC      2C 5C 7D 8S QH      Player 1
        Highest card Ace    Highest card Queen
3       2D 9C AS AH AC      3D 6D 7D TD QD      Player 2
        Three Aces          Flush with Diamonds
4       4D 6S 9H QH QC      3D 6D 7H QD QS      Player 1
        Pair of Queens      Pair of Queens
        Highest card Nine   Highest card Seven
5       2H 2D 4C 4D 4S      3C 3D 3S 9S 9D      Player 1
        Full House          Full House
        With Three Fours    with Three Threes


The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each
player's hand is in no specific order, and in each hand there is a clear
winner.

How many hands does Player 1 win?
"""

import itertools

PROBLEM = 54
SOLVED = True
SPEED = float('0.083')
TAGS = ['poker']


class PokerHand(object):
    # pylint: disable=locally-disabled,too-few-public-methods
    """Object to store and calculate a poker hand"""
    _values = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
        }

    def __init__(self, cards):
        self.cards = cards
        self.values = []
        suits = []
        for card in cards:
            value = int(self._values.get(card[0], card[0]))
            self.values.append(value)
            suits.append(card[1])
        self.values.sort(reverse=True)
        self.is_flush = suits == [suits[0]] * 5
        high_card = self.values[0]
        self.is_straight = self.values == range(high_card, high_card-5, -1)
        self._reorder()

    def _reorder(self):
        """Order the card values to ease comparison"""
        intermediate = []
        for value, group in itertools.groupby(self.values):
            intermediate.append((len(list(group)), value))
        self.values = []
        for count, value in sorted(intermediate, reverse=True):
            self.values += [value] * count

    def __repr__(self):
        classname = self.__class__.__name__
        return '%s(%r)' % (classname, self.cards)

    def __cmp__(self, other):
        """Compare two poker hands"""
        return cmp(self.rank(), other.rank()) \
            or cmp(self.values, other.values)

    def rank(self):
        """Calculate a numerical rank for the hand"""
        # the basic rank is calculated via
        # each group is cubed and summed:
        # 1 pair = 1*2^3 + 3*1^3 = 11
        # 2 pair = 2*2^3 + 1*1^3 = 17
        # 3/kind = 1*3^3 + 2*1^3 = 29
        # fullhs = 1*3^3 + 1*2^3 = 35
        # 4/kind = 1*4^3 + 1*1^3 = 65
        rank = 0
        for _, group in itertools.groupby(self.values):
            rank += len(list(group)) ** 3
        # special cases
        if self.is_straight and self.is_flush:
            rank = 70
        elif self.is_straight:
            rank = 33
        elif self.is_flush:
            rank = 34
        return rank


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    wins = 0
    with open('fixtures/d%04d.txt' % PROBLEM) as hands:
        for hand in hands:
            cards = hand.split()
            hand1 = PokerHand(cards[:5])
            hand2 = PokerHand(cards[5:])
            if hand1 > hand2:
                # print hand1, '>', hand2
                wins += 1
    print wins


if __name__ == '__main__':
    main()
