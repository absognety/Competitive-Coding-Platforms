"""

Given a square matrix arr[ ][ ] of n rows and an integer x, find out whether 
there is a sub-array inside the matrix with sum of elements equal to x. 
The sub-array can be a 2-D array of any number of rows and columns.

Input:
First line of input consists of number of test cases t. 
Then t test cases follow. In each test case, first line 
holds the integer n which represents numbers of rows in square matrix. 
Second line of each test case consists of n*n space separated integers 
representing the matrix arr. Third and last line of test case holds the value x.

Output:
If a sub-array with sum x is found, 'Yes' is printed. Otherwise, 'No' is printed.

Your Task:
Your task is to complete the function is_rectangle_there( ). 
This function takes the matrix, n and x as arguments and returns 0 or 1.

Constraints:
T = 250
2 <= n <= 50
1 <= arr[i][j] <= 1000
1 <= x <= 5000000

Example:
Input:
2
3
1 4 2 4 2 5 7 5 7
30
2
4 5 9 10
8
Output:
Yes
No
Explanation:
Testcase 1 :
Input array:
1 4 2
4 2 5
7 5 7
Sub matrix with sum 30:
4 2 5
7 5 7

"""


def is_rectangle_there(arr,n,x):
    """
    solution goes here
    """
    

if __name__ == '__main__':    
    t=int(input())
    for _ in range(t):
        n = int(input())
        line = input().strip().split()
        arr = [ [ int( line[i*n+j] ) for j in range(n) ] for i in range(n) ]
        x = int(input())
        if is_rectangle_there( arr, n, x) is True:
            print('Yes')
        else:
            print('No')