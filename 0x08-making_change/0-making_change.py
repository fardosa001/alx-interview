#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """fewest number of coins needed to
    meet a given amount total"""

    coins_used = 0
    current = 0
    if total <= 0:
        return 0

    coins = reversed(sorted(coins))

    for coin in coins:
        while current + coin <= total:
            coins_used += 1
            current += coin

    if current != total:
        return -1

    return coins_used
