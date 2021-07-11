"""
Daily Coding Problem #447

This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) 
function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.

"""

import sys
sys.setrecursionlimit(100000)
def powxy(x,y):
    if y == 1:
        return x
    elif y == 0:
        return 1
    elif y > 0:
        return (x * powxy(x,y-1))
    elif y < 0:
        res = x * powxy(x,(-1 * y)-1)
        return 1/res
    
print (powxy(2, 4))
print (powxy(3,89))
print (powxy(4,-34))
print (powxy(5,-46))
print (powxy(4, 1999))