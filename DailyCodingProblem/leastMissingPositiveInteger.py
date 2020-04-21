"""
Daily Coding Problem #4

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear 
time and constant space. In other words, find the lowest positive integer that does 
not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

"""


def missing_integer(arr,n):
    poss = [x for x in arr if x > 0]
    if poss:
        if poss == list(range(1,n+1)):
            return max(poss)+1
        else:
            min_poss = min(poss)
            max_poss = max(poss)
            total_range = list(range(1,max_poss+1))
            if set(total_range) != set(poss):
                missingNumbers = set(total_range) - set(poss)
            else:
                missingNumbers = [max(poss)+1]
            return min(missingNumbers)
    else:
        return 0
    
    
if __name__ == '__main__':
    T = int(input())
    for tcs in range(T):
        arr = list(map(int,input().strip().split()))
        n = len(arr)
        print (missing_integer(arr,n))