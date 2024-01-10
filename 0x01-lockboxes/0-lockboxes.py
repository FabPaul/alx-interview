#!/usr/bin/python3

""" Python Lockboxes. check me out"""


def canUnlockAll(boxes):
    """ method that determines if all boxes can open """

    if type(boxes) is not list or not boxes:
        return False

    unlockedBox = [0]
    for currentBox in unlockedBox:
        for key in boxes[currentBox]:
            if key not in unlockedBox and key < len(boxes):
                unlockedBox.append(key)

    if len(unlockedBox) == len(boxes):
        return True
    return False
