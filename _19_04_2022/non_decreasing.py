#!/usr/bin/python3
def check(lst):
    joker_is_used = False
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            if not joker_is_used:
                joker_is_used = True
            else:
                return False
    return i == len(lst) - 2
