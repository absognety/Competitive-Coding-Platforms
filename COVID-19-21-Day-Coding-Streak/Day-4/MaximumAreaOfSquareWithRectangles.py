#User function Template for python3
"""
Hannah and her cookie box

Hannah loves making cookies. She wants to parcel the biggest possible box of cookies to her friend Ana. 
The box must be square in shape. Each cookie must be placed next to each other in the box ie- 
no overlapping is allowed. The cookies she has made are all rectangular in size such that each is 1 unit wide 
but has varying length. The length of all N cookies are given in an array {C1, C2....Cn}.
These cookies can be rearranged in any order. Help Hannah find the maximum area of the 
square box that can be filled with the cookies.

Input:
First line of input contains number of testcases T. For each testcase, there 
will be two lines, first of which containing the number of cookies N. Next 
line contains N space separated integers denoting the height of each cookie.

Output:
Print the maximum area of the square box that can be filled with the cookies.

Your Task:
Complete the function maxArea()that takes the number of cookies N and array 
containing the height of N cookies as input and returns the desired output.

Constraints: 
1 <= T <= 30
1 <= N<= 105
1<= Length of a Cookie <= 103

Example:
Input: 
2
5
1 3 4 5 5 
5
6 1 6 6 6

Output:
9
16

Explanation:
Testcase 1 : Square with side = 3 can be obtained from either {3, 4, 5} or 
{4, 5, 5}.
"""

def maxArea(a, n) : 
    a = sorted(a)
    maxi = 0
    st = 0
    for i in range(n):
        st = a[i]
        if i+a[i]-1<n:
            maxi = max(maxi,st*st)
        else:
            k = n-i
            maxi = max(maxi,k*k)
    return maxi

def maxArea2(arr,n):
    ans = 1
    arr = sorted(arr)
    for i in range(n):
        ans = max(ans,min(arr[i],n-i))
    return pow(ans,2)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):

        n = int(input())

        arr=[int(x) for x in input().split()]

        print(maxArea(arr,n))
# } Driver Code Ends