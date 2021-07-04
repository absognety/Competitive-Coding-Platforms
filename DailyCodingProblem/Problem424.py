"""
Daily Coding Problem #424

This problem was asked by Facebook.

Given an array of integers in which two elements appear exactly once 
and all other elements appear exactly twice, find the two elements 
that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?

"""

import collections
def findElementsByCount(arr,c):
    collect_elements = set()
    hashMap = collections.Counter(arr)
    for k,v in hashMap.items():
        if v == c:
            collect_elements.add(k)
    return collect_elements

arr = [2, 4, 6, 8, 10, 2, 6, 10]
c = 1
print (findElementsByCount(arr, c))
c = 2
print (findElementsByCount(arr, c))