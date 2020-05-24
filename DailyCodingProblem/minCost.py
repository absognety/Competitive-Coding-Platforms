"""
Daily Coding Problem #19

This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different 
colors. He has a goal of minimizing cost while ensuring that no two neighboring 
houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to 
build the nth house with kth color, return the minimum cost which achieves 
this goal.

Solution:
    This problem statment can be translated into Hungarian assignment problem.
    (min-cost flow problem)

"""
import math
def mincost(arr,row,prevcol,n,k):
    if row == len(arr):
        return 0
    C = len(arr[row])
    dp = [[math.inf for x in range(k+1)] for y in range(n)]
    if dp[row][prevcol+1] != math.inf:
        return dp[row][prevcol+1]
    res = math.inf
    for j in range(C):
        if j != prevcol:
            val = arr[row][j] + mincost(arr,row+1,j,n,k)
            res = min(res,val)
    dp[row][prevcol+1] = res
    return res
    
if __name__ == '__main__':
    N,K = list(map(int,input().strip().split()))
    matrix = [[int(input()) for q in range(K)] for p in range(N)]
    print (mincost(matrix,0,-1,N,K))