"""
Daily Coding problem #129

Given a real number n, find the square root of n. For example, 
given n = 9, return 3.

"""

import math
def sqroot(n):
    return math.sqrt(n)

if __name__ == '__main__':
    for tc in range(int(input())):
        n = float(input())
        print (sqroot(n))