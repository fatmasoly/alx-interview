#!/usr/bin/python3


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
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
