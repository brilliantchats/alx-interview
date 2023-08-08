#!/usr/bin/python3
"""
Minimum Operations
"""


def recurseOperations(op, counter, string, new_string, num):
    """Recursive function for minimum opeartions function"""
    if op == 'copy':
        new_str = new_string + new_string  # When op is copy, do copy and paste
        new_counter = counter + 2
        if len(new_str) == num:
            return new_counter
        if len(new_str) > num:
            return 0
        string = new_string
    if op == 'paste':
        new_str = new_string + string  # When op is paste, do paste only
        new_counter = counter + 1
        if len(new_str) == num:
            return new_counter
        if len(new_str) > num:
            return 0
    copy_all = recurseOperations('copy', new_counter, string, new_str, num)
    paste = recurseOperations('paste', new_counter, string, new_str, num)
    if copy_all <= paste and copy_all != 0:
        minOps = copy_all
    elif copy_all > paste and paste == 0:
        minOps = copy_all
    else:
        minOps = paste
    return minOps


def minOperations(n):
    """
    Find the minimum operations to output n times 'H' in a file
    whose text editor only allows two operations - CopyAll and paste
    """
    if type(n) is not int or n <= 1 or n > 999:
        return 0
    og_str = 'H'
    new_str = og_str + og_str  # Copy and paste the first round
    if len(new_str) == n:
        return 2
    counter = 2
    copy_all = recurseOperations('copy', counter, og_str, new_str, n)
    paste = recurseOperations('paste', counter, og_str, new_str, n)
    if copy_all <= paste and copy_all != 0:
        minOperations = copy_all
    elif copy_all > paste and paste == 0:
        minOperations = copy_all
    else:
        minOperations = paste
    return minOperations
