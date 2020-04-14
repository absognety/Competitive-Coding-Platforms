"""
Given an array of N integers. The task is to find the longest contiguous subarray so 
that the average of its elements is greater than or equal to a given number X.

Examples:

Input:  arr = {1, 1, 2, -1, -1, 1},  X = 1
Output: 3
Length of longest subarray
with average >= 1 is 3 i.e.
((1+1+2)/3)= 1.333

Input: arr[] = {2, -3, 3, 2, 1}, x = 2
Output: 3
Length of Longest subarray is 3 having 
average 2 which is equal to x.

"""
def maxIndexDiff(arr,n):
    LMin = [None] * n
    RMax = [None] * n
    LMin[0] = arr[0]
    for i in range(1,n):
        LMin[i] = min(arr[i],LMin[i-1])
    RMax[n-1] = arr[n-1]
    for j in range(n-2,-1,-1):
        RMax[j] = max(arr[j],RMax[j+1])
    i,j,maxDiff = 0,0,-1
    while ((j < n) & (i < n)):
        if LMin[i] < RMax[j]:
            maxDiff = max(maxDiff,j - i)
            j += 1
        else:
            i += 1
    return (maxDiff + 1)

def modifyArr(arr,n,x):
    for i in range(n):
        arr[i] = arr[i] - x
        
def calcPrefix(arr,n):
    s = 0
    for i in range(n):
        s += arr[i]
        arr[i] = s
        
def longestSubArray(arr,n,x):
    modifyArr(arr,n,x)
    calcPrefix(arr,n)
    return maxIndexDiff(arr,n)

### Testcases
print (longestSubArray([1,1,2,-1,-1,1],6,1))
print (longestSubArray([2,-3,3,2,1],5,2))