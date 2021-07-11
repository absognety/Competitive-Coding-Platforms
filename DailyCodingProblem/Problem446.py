"""
Daily Coding Problem #446

This problem was asked by Indeed.

Given a 32-bit positive integer N, determine whether it is a power 
of four in faster than O(log N) time.

"""

import math
def isPowerOf4(N:int) -> bool:
    d = str(math.log(N,4))
    if d.split(".")[1] == "0":
        return True
    else:
        return False
    
print (isPowerOf4(256))
print (isPowerOf4(128))
print (isPowerOf4(1024))
print (isPowerOf4(1023))