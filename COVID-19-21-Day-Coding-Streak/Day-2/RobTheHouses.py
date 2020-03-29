#User function Template for python3

#Complete this function

"""
In Byteland there is a circular colony of N houses . 
Each house in the colony has some money. The value of money can either be 
positive or negative. Find the maximum amount of money you can have after 
robbing any number of contiguous houses.

Note: Robbing a house having negative money will reduce your money by that 
amount.


Input:
First line of input contains a single integer T which denotes the number 
of test cases. First line of each test case contains a single integer N which 
denotes the total number of houses. Second line of each test case contains N 
space separated integers denoting money in the houses.


Output:
For each test case print the maximum money by robbing the consecutive houses.
User Task:
The task is to complete the function maxMoney() which returns the maximum 
money.

Constraints:
1 <= T <= 100
1 <= N <= 106
-106 <= Arr[i] <= 106

Example:
Input:
3
7
8 -8 9 -9 10 -11 12
8
10 -3 -4 7 6 5 -4 -1
8
-1 40 -14 7 6 5 -4 -1
Output:
22
23
52


Explanation:
Testcase 1: Starting from last house of the colony, robbed 12 units and 
moving in circular fashion, we can rob  8, -8, 9, -9, 10, which gives 
maximum robbed monney as 22.


"""

def kadane(arr,n):
    max_so_far = max_ending_here = 0
    for a in range(n):
        max_ending_here = max_ending_here + arr[a]
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far

def maxMoney(arr,n):
    ##Your code here
    max_kadane = kadane(arr,n)
    max_wrap = 0
    for i in range(n):
        max_wrap += arr[i]
        arr[i] = -1 * arr[i]
    max_wrap = max_wrap + kadane(arr,n)
    if max_wrap > max_kadane:
        return max_wrap
    else:
        return max_kadane

#{ 
#  Driver Code Starts
#Initial Template for Python 3



import math


    
    
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            print(maxMoney(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()


# } Driver Code Ends