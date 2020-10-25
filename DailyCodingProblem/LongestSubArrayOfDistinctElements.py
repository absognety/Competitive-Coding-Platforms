"""
Daily Coding Problem #189

This problem was asked by Google.

Given an array of elements, return the length of the longest 
subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 
as the longest subarray of distinct elements is [5, 2, 3, 4, 1].

"""

###Using itertools
import itertools
def longest_subarray_distinct(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return len(arr)
    for l in range(len(arr),0,-1):
        subarrays = set(itertools.combinations(arr, l))
        for suba in subarrays:
            if len(suba) == len(set(suba)):
                return len(suba)
    return 0

print (longest_subarray_distinct([5, 1, 3, 5, 2, 3, 4, 1]))