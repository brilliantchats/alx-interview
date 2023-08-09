#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Find the minimum operations to output n times 'H' in a file
    whose text editor only allows two operations - CopyAll and paste
    """
    counter = 0
    i = 2
    max_num = n
    while i <= max_num:
        while max_num % i == 0:
            counter = counter + i
            max_num = max_num / i
        i = i + 1
    return counter
