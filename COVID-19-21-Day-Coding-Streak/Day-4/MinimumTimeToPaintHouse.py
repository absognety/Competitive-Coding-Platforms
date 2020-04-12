#User function Template for python3
# Brute Force Approach - Recursive solution
"""
Lucy's Home

Nancy has a cat named Lucy. She wants to paint her home which is made of N 
wooden boards of different lengths denoted by [A1, A2,..., An]. She hires K painters to do this work. 
Each painter takes 1 unit of time to paint 1 unit of board. Help her find the minimum time to get this 
job done under the constraint that a painter can only paint multiple boards 
if they are contiguous to each other. This means a configuration where painter 1 paints board 1 and 
board 3 but not board 2 is invalid.

Input:
The first line consists of a single integer T, the number of test cases. For each test case, the first line contains 
an integer k denoting the number of painters and integer n denoting the number of boards. Next line contains n- space 
separated integers denoting the size of boards.

Output:
For each test case, the output is an integer displaying the minimum time for 
painting that house.

Constraints:
1<=T<=100
1<=k , n <= 103
1<=A[i]<=104

Example:
Input:
2
2 4
10 10 10 10
2 4
10 20 30 40
Output:
20
60

Explanation:
1. Here we can divide the boards into 2 equal sized partitions, so each 
painter gets 20 units of the board and the total time taken is 20.
2. Here we can divide first 3 boards for one painter and the last board for 
the second painter.
"""

def Min_Time(arr,n,k):
    #code here
    if k == 1:
        return sum(arr[0:n])
    if n == 1:
        return arr[0]
    best = 10000
    for i in range(1,n+1):
        best = min(best,max(Min_Time(arr,i,k-1),sum(arr[i:n])))
    return best


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