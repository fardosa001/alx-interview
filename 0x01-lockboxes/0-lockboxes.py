#!/usr/bin/python3
"""Write a method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened"""
    for key in range(1, len(boxes)):
        flag = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                flag = True
                break
        if not flag:
            return False

    return True
