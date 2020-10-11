"""
Daily Coding Problem: Problem #155

This problem was asked by MongoDB.

Given a list of elements, find the majority element, 
which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.

"""

import collections
import math
def majority_element(arr):
    hash_map = collections.Counter(arr)
    l = len(arr)
    for key,value in hash_map.items():
        if value >= math.floor(l / 2.0):
            return key
    return -1

print (majority_element([1, 2, 1, 1, 3, 4, 0]))