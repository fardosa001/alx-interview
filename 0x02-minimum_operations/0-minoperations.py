#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """calculates the fewest number of operations
    needed to result in exactly n H characters in the file."""
    current_length = 1
    copied_content = ""
    operations = 0
    str_char = "H"

    while current_length < n:
        if n % current_length == 0:
            copied_content = str_char
            operations += 1
        str_char += copied_content
        current_length = len(str_char)
        operations += 1
    return operations
