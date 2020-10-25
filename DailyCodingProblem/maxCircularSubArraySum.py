"""
Daily Coding Problem #190

This problem was asked by Facebook.

Given a circular array, compute its maximum subarray sum in O(n) 
time. A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the 
numbers 3, 4, and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.

"""

def kadane_algorithm(arr,n):
    max_so_far = max_ending_here = 0
    for a in range(n):
        max_ending_here = max_ending_here + arr[a]
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far

def maxSum(arr,n):
    ##Your code here
    max_kadane = kadane_algorithm(arr, n)
    max_wrap = 0
    for i in range(n):
        max_wrap += arr[i]
        arr[i] = -1 * arr[i]
    max_wrap = max_wrap + kadane_algorithm(arr,n)
    if max_wrap > max_kadane:
        return max_wrap
    else:
        return max_kadane
    
if __name__ == '__main__':
    for tcase in range(int(input())):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        print (maxSum(arr,n))