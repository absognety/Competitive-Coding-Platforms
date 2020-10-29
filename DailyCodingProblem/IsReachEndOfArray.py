"""
This problem was asked by Google.

You are given an array of nonnegative integers. Let's say you start 
at the beginning of the array and are trying to advance to the end. 
You can advance at most, the number of steps that you're currently on. 
Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from 
indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
"""

import math
def min_jumps(arr,n):
    if n==1:
        return 0
    res = math.inf
    for i in range(n-2,-1,-1):
        if (i + arr[i]) >= n-1:
            sub_res = min_jumps(arr,i+1)
            if (sub_res != math.inf):
                res = min(res,sub_res + 1)
    return res

def advance_to_end(arr,n):
    x = min_jumps(arr,n)
    if x > 0 and x != math.inf:
        return "true"
    elif x == 0 or x == math.inf:
        return "false"

if __name__ == '__main__':
    for tcase in range(int(input())):
        arr = list(map(int,input().strip().split()))
        print (advance_to_end(arr,len(arr)))