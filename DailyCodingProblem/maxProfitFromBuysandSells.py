"""
Daily Coding problem #130

This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a 
company in chronological order and an integer k, return the 
maximum profit you can make from k buys and sells. You must 
buy the stock before you can sell it, and you must sell the 
stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should 
return 3.

Solution:
    https://www.youtube.com/watch?v=Pw6lrYANjz4&t=1004s

"""
import math
def maxProfitWithKTransactions(arr,k):
    if len(arr) == 0:
        return 0
    profit = [[0 for d in arr] for t in range(k+1)]
    for t in range(1,k+1):
        maxThusFar = -math.inf
        for d in range(1,len(arr)):
            maxThusFar = max(maxThusFar,
                             profit[t-1][d-1] - arr[d-1])
            profit[t][d] = max(profit[t][d-1],
                               maxThusFar + arr[d])
    return profit[-1][-1]

if __name__ == '__main__':
    for tcase in range(int(input())):
        k = int(input())
        arr = list(map(int,input().strip().split()))
        print (maxProfitWithKTransactions(arr, k))