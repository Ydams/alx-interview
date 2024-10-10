#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n  # List to track unlocked boxes
    unlocked[0] = True  # The first box is unlocked
    keys = boxes[0]  # Start with the keys in the first box
    unlocked_count = 1  # Number of unlocked boxes

    while keys:
        key = keys.pop()  # Take one key at a time
        if key < n and not unlocked[key]:  # Check if the key is valid and the box is locked
            unlocked[key] = True  # Unlock the box
            unlocked_count += 1  # Increment the unlocked box count
            keys.extend(boxes[key])  # Add new keys from this box to the key list

    return unlocked_count == n  # Return True if all boxes are unlocked, False otherwise

