"""
Given a positive integer B denoting the base of a right angled isosceles triangle. Find the maximum number of squares of size 2×2 units that can fit in it.

Input:
First line of input contains an integer T denoting number of test cases. For each test case, there exists one line containing integer B ie-base of right angled isosceles triangle.

Output:
For each test case, print the maximum number of squares that can be fit into the triangle.

Constraints:
1<= T <=100
1<= B <= 1000

Example:

Input:
2
8
2

Output:
6
0
"""

def triangleAndSquare(base):
    if base <= 2:
        return 0
    else:
        if base%2 == 0:
            base = base - 2
            base = base / 2
            return int((base * (base + 1)/2))
        else:
            base = base - 1
            base = base - 2
            base = base / 2
            return int((base * (base + 1)/2))
    
    
if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        b = int(input())
        print (triangleAndSquare(b))