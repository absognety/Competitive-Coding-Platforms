"""
Given an array A of integers and an integer X. Find the length of maximum size 
subarray having an average of integers greater than or equal to X. 

For Example:
Input : A[] = {-2, 1, 6, -3}, X = 3
Output : 2
Longest subarray is {1, 6} having average 3.5 greater than X = 3.

Input:
The first line of input contains T denoting the number of test cases. Then T test 
cases follow. Each test case contains two lines of input. The first line contains the 
number N and X. The second line contains the array A.

Output:
For each test case, in a new line, print the length of the maximum size subarray 
having an average greater than equal to X.

Your Task:
You don't have to take input. You need to complete the function LongestSub(), which 
takes array arr, N and X as a parameter and returns the answer. The printing is done by 
the driver code.

Constraints:
1 <= T <= 10
1 <= N, X <= 10^5
1 <= abs(A[i]) <= 10^5
abs represent the absolute value of A[i]
Sum of N over all test cases doesn't exceed 10^5

Example:
Input:
3
10 7
2 3 6 -5 -3 7 9 7 -9 7
4 3
-2 1 6 -3 
5 2
2 -3 3 2 1
Output:
3
2
3
"""

#User function Template for python3

def findInd(preSum,n,val):
    l=0
    h=n-1
    ans = -1
    while (l <= h):
        mid = (l + h)//2
        if preSum[mid][0] <= val:
            ans = mid
            l = mid + 1
        else:
            h = mid - 1
    return ans

def LongestSub(arr,n,x):
    #code here
    for i in range(n):
        arr[i] -= x
    maxlen = 0
    total = 0
    minInd = [None] * n
    preSum = []
    for i in range(n):
        total += arr[i]
        preSum.append((total,i))
    preSum = sorted(preSum)
    minInd[0] = preSum[0][1]
    for i in range(1,n):
        minInd[i] = min(minInd[i-1],preSum[i][1])
    total = 0
    for i in range(n):
        total += arr[i]
        if total >= 0:
            maxlen = i + 1
        else:
            ind = findInd(preSum,n,total)
            if (ind != -1) & (minInd[ind] < i):
                maxlen = max(maxlen,i - minInd[ind])
    return maxlen



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ =='__main__':
    from math import inf
    tcs=int(input())

    for _ in range(tcs):
        N,X=[int(e) for e in input().split()]
        arr=[int(e) for e in input().split()]

        print(LongestSub(arr,N,X))
# } Driver Code Ends