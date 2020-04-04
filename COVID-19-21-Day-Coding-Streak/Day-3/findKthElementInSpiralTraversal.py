"""
Given a matrix of size N x M . You have to find the kth element 
which will obtain while traversing the matrix spirally.


Input:
The first line of input is the no of test cases then T test 
cases follow . The first line of each test case has three 
integers n(rows), m(columns) and k . Then in the next line are 
n*m space separated values of the matrix A [ ] [ ] .


Output:
For each test case print spirally obtained kth element .


Your Task:
Since this is a functional problem you do need to take input 
just complete the function findK which accepts four parameters. 
The first parameter is the matrix A and the next two parameters 
are  n and m denoting the size of the matrix A . The fourth 
parameter is an integer  k denoting the kth element . The function will return the 
kth element obtained while traversing the matrix spirally.


Constraints:
1<=T<=100
1<=n,m<=20
1<=k<=n*m


Example:
Input
2
3 3 4
1 2 3 4 5 6 7 8 9 
2 2 2
1 2 3 4


Output
6
2


Explanation
The matrix above will look like 
1 2 3
4 5 6
7 8 9
and the 4th element in spiral fashion will be 6 .
"""

def findK(arr, m, n, q):
    #Code here
    spiralPath = []
    k = 0
    l = 0
    while (k < m and l < n) : 
        for i in range(l, n) : 
            spiralPath.append(arr[k][i])
        k += 1
        
        for i in range(k, m) : 
            spiralPath.append(arr[i][n - 1])
        n -= 1
        
        if (k < m):
            for i in range(n - 1, (l - 1), -1):
                spiralPath.append(arr[m - 1][i])
            m -= 1
            
        if (l < n): 
            for i in range(m - 1, k - 1, -1): 
                spiralPath.append(arr[i][l])
            l += 1
    #print (spiralPath)
    return spiralPath[q-1]

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])]for j in range(n[0])]
        c=0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c+=1
        print(findK(matrix, n[0], n[1], n[2]))