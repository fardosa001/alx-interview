#!/usr/bin/python3
"""Write a method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened"""
    if not boxes:
        return False

    keys = set([0])  # Set to keep track of the keys obtained
    unlocked = set([0])
    while keys:
        box = keys.pop()  # Get a box with keys
        for key in boxes[box]:  # Check keys inside the box
            if key not in unlocked:  # If the box is not yet unlocked
                unlocked.add(key)  # Unlock the box
                keys.add(key)

    return len(unlocked) == len(boxes)
