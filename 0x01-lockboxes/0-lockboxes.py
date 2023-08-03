#!/usr/bin/python3
"""
Lockbox Challenge
"""


def canUnlockAll(boxes):
    """ A solution to the lockbox challenge """
    keys = dict()
    locked_boxes = list()
    if len(boxes) <= 1:
        return True
    unlockable = True
    for i in range(len(boxes)):
        if i == 0:
            for item in boxes[i]:
                if item not in keys:
                    keys[item] = item
        else:
            if i not in keys:
                locked_boxes.append(i)
                unlockable = False
                for item in boxes[i]:
                    if item not in keys and item != i:
                        keys[item] = item
            else:
                for item in boxes[i]:
                    if item not in keys:
                        keys[item] = item
    if unlockable:
        return True
    for num in locked_boxes:
        if num not in keys:
            return False
    return True
