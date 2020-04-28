"""
Daily Coding Problem #9

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum 
of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

"""
import itertools
import math
def largestSum(arr,n):
    evens = arr[0:n:2]
    odds = arr[1:n:2]
    maxSum1 = -1 * math.inf
    maxSum2 = -1 * math.inf
    for i in range(1,len(evens)+1):
        combinations = list(itertools.combinations(evens,i))
        for c in combinations:
            if sum(c) > maxSum1:
                maxSum1 = sum(c)
    for i in range(1,len(odds)+1):
        combinations = list(itertools.combinations(odds,i))
        for c in combinations:
            if sum(c) > maxSum2:
                maxSum2 = sum(c)
    i = 0
    maxSum3 = -1 * math.inf
    while i < len(evens):
        j = i + 1
        while (j < len(odds)):
            new_list = [evens[i]]+odds[j:]
            print (new_list)
            for k in range(1,len(new_list)+1):
                combinations = list(itertools.combinations(new_list,k))
                for c in combinations:
                    if sum(c) > maxSum3:
                        maxSum3 = sum(c)
            j += 1
        i += 1
    
    j = 0
    maxSum4 = -1 * math.inf
    while j < len(odds):
        i = j + 2
        while (i < len(evens)):
            new_list = [odds[j]]+evens[i:]
            print (new_list)
            for k in range(1,len(new_list)+1):
                combinations = list(itertools.combinations(new_list,k))
                for c in combinations:
                    if sum(c) > maxSum4:
                        maxSum4 = sum(c)
            i += 1
        j += 1
    return max(maxSum1,maxSum2,maxSum3,maxSum4)


## O(N) implementation
## Simple Code from GeeksForGeeks
    
def findMaxSum(arr,n):
    incl = arr[0]
    excl = 0
    
    for i in range(1,n):
        excl_new = incl if incl > excl else excl
        incl = excl + arr[i] 
        excl = excl_new
        
    if incl > excl:
        return incl
    else:
        return excl

    
if __name__ == '__main__':
    T = int(input())
    for tcs in range(T):
        arr = list(map(int,input().strip().split()))
        n = len(arr)
        print (largestSum(arr,n))
        print (findMaxSum(arr,n))