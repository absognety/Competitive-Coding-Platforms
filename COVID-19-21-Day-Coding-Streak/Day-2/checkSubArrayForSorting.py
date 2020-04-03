#User function Template for python3

"""
John's school has been cancelled due to the Corona Pandemic for 
a few weeks. He is stuck at home and his mother has given him 
the task of arranging all his tshirts in sorted order. He has N 
tshirts all of which are denoted by a distinct numeric value. 
But John is lazy and wants to be done with this task as soon as 
possible. Help John find a sub array in the given order of 
tshirts, such that reversing the subarray will be sufficient to 
arrange all his tshirts in sorted order.

Input:
The first line of input contains the number of testcases T. The 
first and only line of every testcase contains an integer N for 
the number of tshirts followed by N space separated integers 
denoting their current order.

Output: 
Return true if a sorted array is possible otherwise return false.

Your Task:
You don't have to take input. Complete the function 
SortedArray() that takes array arr and n as parameter and 
return the true or flase. The printing is done by the driver code.

Constraints:
1<= T <= 50
1 <= N <= 102

Example:
Input:
2
5 1 2 5 4 3
5 1 2 4 5 3
Output:
Yes
No

Explanation:
Testcase 1: Reverse the subarray {5, 4, 3} to get the sorted 
array {1, 2, 3, 4, 5}.
Testcase 2: No matter what subarray you reverse, the original 
array will never be sorted.
"""

def can_sort(arr,n):
    # code here
    temp = [0]*len(arr)
    for i in range(n):
        temp[i] = arr[i]
    temp = sorted(temp)
    for front in range(0,n):
        if (temp[front] != arr[front]):
            break
    for back in range(n-1,-1,-1):
        if temp[back] != arr[back]:
            break
    if front >= back:
        return True
    while True:
        front += 1
        if (arr[front-1] < arr[front]):
            return False
        if not (front != back):
            break
    return True


#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    line=input().strip().split()
    n=int(line[0])
    arr=[]
    for i in range(n):
        arr.append(int(line[i+1]))
    if(can_sort(arr,n)):
        print('Yes')
    else:
        print('No')
# } Driver Code Ends