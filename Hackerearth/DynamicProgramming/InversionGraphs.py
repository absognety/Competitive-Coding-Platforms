"""
You are given an array A with N elements. You create a graph G with 
N vertices using A as follows:

For any pair of indices (i,j)  where 1 <= i < j <= N , if A[i] > A[j], 
then add an undirected edge between vertices i and j .

In graph G, find the maximum possible size of set S (of vertices in G) 
such that there exists an edge between every pair of vertices that are available 
in S.

Input format

The first line contains an integer  N denoting the number of elements in A .
The second line contains N space-separated integers denoting the elements of A.
Output format

Among all the vertices available in S, find the maximum possible size of S.

Constraints
 1 <= N <= 10**5
 1 <= A[i] <= 10**6

SAMPLE INPUT 
3
2 1 3

SAMPLE OUTPUT 
2

Explanation
G will have 3 vertices and following edges : 1 - 2

S = {1, 2 } , |S| = 2 is optimal choice.

"""