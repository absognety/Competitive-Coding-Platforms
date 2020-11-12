"""
Daily Coding Problem #209

This problem was asked by YouTube.

Write a program that computes the length of the longest common 
subsequence of three given strings. For example, given "epidemiologist", 
"refrigeration", and "supercalifragilisticexpialodocious", it should 
return 5, since the longest common subsequence is "eieio".

"""
#Substrings need to be contiguous where as subsequences are not.
#Two types of solutions:
#   1. Overlapping subproblems using recursion
#   2. DP problem

def lcs(X,Y):
    m = len(X)
    n = len(Y)
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if (i==0) or (j==0):
                dp[i][j] = 0
            elif X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

if __name__ == '__main__':
    X = "AGGTAB"
    Y = "GXTXAYB"
    print ("Length of longest common subsequence: ",lcs(X,Y))
    st1 = "epidemiologist"
    st2 = "refrigeration"
    st3 = "supercalifragilisticexpialodocious"
    print ("Length of longest common subsequence: ",
                min(lcs(st1,st2),lcs(st2,st3),lcs(st1,st3)))