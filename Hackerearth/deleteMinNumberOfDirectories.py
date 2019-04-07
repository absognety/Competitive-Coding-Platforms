'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
"""
Directory Deletion
You are given a directory tree of N directories/folders. Each directory is represented by a particular id which ranges from 0 to N. The id of the root directory is 1 , then it has some child directories, those directories may contain some other ones and it goes on. Now you are given a list of directory id's to delete, you need to find the minimum number of directories that need to be deleted so that all the directories in the given list get deleted. 

Note that if you delete a particular directory, all its child directories will also get deleted.

Input
The first line of input contains an integer N that denotes how many folders are there.
The next line contains N space separated integers that where the ith integer denotes the id of the parent of the directory with id i. Note that the first integer will be -1 as 1 is the id of root folder and it has no parent. Rest of the integers will not be -1.
The next line contains an integer M that denotes how many directories you need to delete.
The next line contains M space separated integers that denote the ids of the directories you need to delete.

Output
Print the minimum number of directories that need to be deleted.

Constraints
1<=N<=10**5
1<=id of parent<=N
1<=M<=N
1<=id to be deleted <=N
"""
# Partially accepted solution here
def delMinNumDirect(arr_n,arr_m):
    n = len(arr_n)
    m = len(arr_m)
    Nodes = [i+1 for i in range(n)]
    id_map = {str(i):j for i,j in zip(Nodes,arr_n)}
    id1Nodes = [i for i in arr_m if id_map[str(i)]==1]
    return (len(id1Nodes))


if __name__ == '__main__':
    N = int(input())
    arr_n = list(map(int,input().strip().split()))
    M = int(input())
    arr_m = list(map(int,input().strip().split()))
    print (delMinNumDirect(arr_n,arr_m))
