"""
Daily Coding Problem #203

This problem was asked by Uber.

Suppose an array sorted in ascending order is rotated at some pivot 
unknown to you beforehand. Find the minimum element in O(log N) time. 
You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.

"""

def binary_search(arr):
    l = 0
    h = len(arr) - 1
    while (arr[l] > arr[h]):
        mid = (l + h)//2
        if arr[mid] > arr[h]:
            l = mid + 1
        else:
            h = mid
    return arr[l]

print (binary_search([5,7,10,3,4]))