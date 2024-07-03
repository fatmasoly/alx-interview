#!/usr/bin/python3
"""Defines canUnlockAll function"""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False"""
    unlocked_boxes = [0]
    keys = []
    keys.extend(boxes[0])
    boxes_length = len(boxes)

    while keys:
        key = keys.pop()

        if key not in unlocked_boxes and key < boxes_length:
            keys.extend(boxes[key])
            unlocked_boxes.append(key)

    return len(unlocked_boxes) == boxes_length
