"""
Daily Coding Problem #197

This problem was asked by Amazon.

Given an array and a number k that's smaller than the length of the
array, rotate the array to the right k elements in-place.

"""

def rotate_inplace(arr,k):
    i = 1
    while (i <= k):
        arr.append(arr[i-1])
        i += 1
    return arr[k:]

print (rotate_inplace([1,2,3,4,5,5,6],4))