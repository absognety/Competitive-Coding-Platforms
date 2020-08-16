"""
Daily Coding Problem #122

This question was asked by Zillow.

You are given a 2-d matrix where each cell represents number of 
coins in that cell. Assuming we start at matrix[0][0], and can 
only move right or down, find the maximum number of coins you 
can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1

The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.

"""

def maxCost(arr,R,C):
    
    #declare the maxCost matrix
    maxcost_arr = [[0 for i in range(C)] for j in range(R)]
    maxcost_arr[0][0] = arr[0][0]
    
    #initialize first row of MaxCost matrix
    for j in range(1,C):
        maxcost_arr[0][j] = maxcost_arr[0][j-1] + arr[0][j]
        
    #Initialize first column of MaxCost Matrix
    for i in range(1,R):
        maxcost_arr[i][0] = maxcost_arr[i-1][0] + arr[i][0]
    
    #This bottom-up approach ensures that all the sub-problems needed
    #have already been calculated.
    for i in range(1,R):
        for j in range(1,C):
            #Calculate cost of visiting (i,j) using the
            #recurrence relation discussed above
            maxcost_arr[i][j] = max(maxcost_arr[i-1][j],
                                    maxcost_arr[i][j-1]) + arr[i][j]
    return maxcost_arr[R-1][C-1]
    
if __name__ == '__main__':
    for tcase in range(int(input())):
        N,M = list(map(int,input().strip().split()))
        cost_arr = []
        for n in range(N):
            row = list(map(int,input().strip().split()))
            cost_arr.append(row)
        print (maxCost(cost_arr,N,M))