#!/usr?bin?python3
'''module for lockboxes'''

def canUnlockAll(boxes):
    unlocked = [0]
    for boxId, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != boxId:
                unlocked.apped(key)
    if len(unlocked) == len(boxes):
        return True
    return False
