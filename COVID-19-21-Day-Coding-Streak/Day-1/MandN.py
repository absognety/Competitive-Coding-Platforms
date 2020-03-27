"""
Given two positive integers M and N, after adding M and N if number of digits 
in M+N and N are same return N otherwise return M+N.

Input:
First line of input contains T denoting number of testcases. For each test 
case there will be two space seperated positive integers M and N.

Output:
If number of digits in M+N is same as N print N otherwise print M+N.

Constraints:
1 <= T <= 100
1 <= M <= 109
1 <= N <=109

Example:
Input:
2
44 22
99 12

Output:
22
111
"""


def MandN(M,N):
    r = M + N
    if len(str(r)) == len(str(N)):
        return N
    else:
        return r
    
if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        M,N = list(map(int,input().strip().split()))
        print (MandN(M, N))