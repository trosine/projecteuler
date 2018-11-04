#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: 0059

https://projecteuler.net/problem=59

XOR decryption

Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange). For
example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key. The advantage
with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and without
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password key
for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower
case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a
file containing the encrypted ASCII codes, and the knowledge that the plain
text must contain common English words, decrypt the message and find the sum of
the ASCII values in the original text.
"""

import itertools

PROBLEM = 59
SOLVED = True
SPEED = float('1.897')
TAGS = ['xor', 'decryption']


def decrypt(message, key):
    """Decrypt message using key"""
    keylen = len(key)
    decrypted = []
    total = 0
    for char in xrange(0, len(message)):
        decrypt_char = message[char] ^ key[char % keylen]
        decrypted.append(chr(decrypt_char))
        total += decrypt_char

    return (total, ''.join(decrypted))


def load_data():
    """Load data file"""
    with open('fixtures/d%04d.txt' % PROBLEM) as datafile:
        data = datafile.readline()
    return [int(char) for char in data.split(',')]


def main():
    """Solve problem."""
    print 'Project Euler: %04d' % PROBLEM
    message = load_data()
    for key in itertools.product(xrange(ord('a'), ord('z')+1), repeat=3):
        total, decrypted = decrypt(message, key)
        if ' the ' in decrypted:
            print total, ''.join([chr(letter) for letter in key]), decrypted
            return


if __name__ == '__main__':
    main()
