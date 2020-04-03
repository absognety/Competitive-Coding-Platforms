#User function Template for python3

"""
Amy, Bob, Charlie and Dylan are stuck together in quarantine. 
They are childhood friends and are playing old games to pass 
the time. Help them find valid corners in the house to play the 
game of corners. 
Their house is represented by a N x M binary matrix consisting 
of 0s and 1s. Here each 1 represents a corner. 
Find if there exists a rectangle/ square within the matrix 
whose all four corners are 1. 

Input: 
The first line of input will be the number of testcases T, 
then T test cases follow. The first line of each testcase 
contains R which denotes the number of rows. The second line 
of each testcase contains C which denotes the number of 
columns. The next line contains the NxM inputs of the matrix 
separated by space.

Output: 
Print "Yes" if there exists a rectangle/ square within the 
matrix whose all four corners are 1; else print "No".

User Task:
Complete the function ValidCorners that takes the given 
matrix as input and returns a boolean value.

Constraints:
1 <= R, C <= 200
0 <= A[i] <= 1


Example:
Input :
2
4
5
1 0 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 1 0 1 
3
3
0 0 0 0 0 0 0 0 0 

Output :
Yes
No

Explanation :
Testcase 1 : Given matrix looks like this
1 0 0 1 0 
0 0 1 0 1 
0 0 0 1 0 
1 0 1 0 1 
Valid corners are at index (1,2), (1,4), (3,2), (3,4) 

"""

def ValidCorner(matrix): 
    # Your code goes here 
    rows = len(matrix)
    if rows == 0:
        return False
    columns = len(matrix[0])
    table = dict()
    for i in range(rows):
        for j in range(columns-1):
            for k in range(j+1,columns):
                if (matrix[i][j] == 1) & (matrix[i][k]==1):
                    if (j in table):
                        if (k in table.get(j)):
                            return True
                    if (k in table):
                        if (j in table.get(k)):
                            return True
                    if (j not in table):
                        x = set()
                        x.add(k)
                        table[j] = x
                    else:
                        table.get(j).add(k)
                    if (k not in table):
                        x = set()
                        x.add(j)
                        table[k] = x
                    else:
                        table.get(k).add(j)
    return False


#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		r = int(input())
		c = int(input())
		line = input().strip().split()
		mat = [ [0 for _ in range(c)] for _ in range(r) ]
		for i in range(r):
			for j in range(c):
				mat[i][j] = int( line[i*c+j] )
		if (ValidCorner(mat)): 
			print("Yes") 
		else: 
			print("No") 


# } Driver Code Ends