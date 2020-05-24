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
def mincost(arr,n,k):
    pass
    
if __name__ == '__main__':
    N,K = list(map(int,input().strip().split()))
    matrix = [[int(input()) for q in range(K)] for p in range(N)]
    print (mincost(matrix,N,K))