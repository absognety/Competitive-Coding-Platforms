#User function Template for python3
#DP solution
"""
Refer the problem statement from 
"""

def Min_Time(arr,n,k):
    #code here
    # initialize table 
    dp = [[0 for i in range(n + 1)]  
             for j in range(k + 1)]  
  
    # base cases 
    # k=1 
    for i in range(1, n + 1): 
        dp[1][i] = sum(arr[0:i])
  
    # n=1 
    for i in range(1, k + 1): 
        dp[i][1] = arr[0] 
  
    # 2 to k partitions 
    for i in range(2, k + 1): # 2 to n boards 
        for j in range(2, n + 1): 
              
            # track minimum 
            best = 10000
              
            # i-1 th separator before position arr[p=1..j] 
            for p in range(1, j + 1):  
                best = min(best, max(dp[i - 1][p],  
                                 sum(arr[p:j])))      
  
            dp[i][j] = best 
  
    # required 
    return dp[k][n]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):

        k,n=[int(x) for x in input().split()]

        arr=[int(x) for x in input().split()]

        print(Min_Time(arr,n,k))
# } Driver Code Ends