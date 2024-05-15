#!/usr/bin/python3
"""Prime Game"""


def is_prime(num):
    """check for prime no."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """return winner of the most rounds"""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
            continue

        if n % 2 == 0 or is_prime(n):
            maria_wins += 1
            continue

        ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
