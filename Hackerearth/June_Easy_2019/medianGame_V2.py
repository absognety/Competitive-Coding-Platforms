"""
You are given an array A of N integers. You perform this operation N-2 times: 
For each contiguous subarray of odd size greater than 2, you find the median of each subarray
(Say medians obtained in a move are M1,M2,......Mk). In each move, you remove the first occurrence of value
min(M1,M2,M3,.......Mk) from the original array. After removing the element the array size reduces by 1 and no void spaces are left. 
For example, if we remove element 2 from the array {1,2,3,4} , the new array will be {1,3,4}.

Print a single integer denoting the sum of numbers that are left in the array after performing the operations. You need to do this for T test cases.

Input Format

The first line contains T denoting the number of test cases(1<=T<=10). 

The first line of each test case contains N denoting the number of integers in the array initially(4<=N<=10^5).

The next line contains N space seperated integers denoting [A1,A2,A3,.....AN] (1<=Ai<=10^9) for all valid i

Output Format

Output a single integer denoting the sum of numbers left in the array after performing the operations for each test case on a new line.

Sample Input

2
4
2 5 3 2
4
1 1 1 1

Sample output

7
2

"""

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(max(arr)+min(arr))