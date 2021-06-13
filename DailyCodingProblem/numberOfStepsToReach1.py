"""
Daily Coding Problem #419

This problem was asked by PagerDuty.

Given a positive integer N, find the smallest number of steps it 
will take to reach 1.

There are two kinds of permitted steps:

You may decrement N to N - 1.
If a * b = N, you may decrement N to the larger of a and b.
For example, given 100, you can reach 1 in five steps with the 
following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.

"""
import math
def getMinDivisors(n) :
    # Note that this loop runs till square root
    i = 1
    all_max_divisors = []
    while (i <= math.sqrt(n)):
         
        if (n % i == 0) :
             
            # If divisors are equal, print only one
            if (n // i == i) :
                if i not in all_max_divisors:
                    all_max_divisors.append(i)
            else :
                # Otherwise print both
                max_d = max(i,n//i)
                all_max_divisors.append(max_d)
        i = i + 1
    return min(all_max_divisors)
        
def minimum_steps(N):
    numofways = 0
    while (N > 1):
        X = getMinDivisors(N)
        #print (N-1, X)
        N = min(N-1,X)
        numofways += 1
    return numofways

print (minimum_steps(100))
print (minimum_steps(10019))
print (minimum_steps(2883838))
print (minimum_steps(45))