"""
Daily Coding Problem #420

This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 
10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you 
should return 28.

"""

def getPerfectNumber(n):
    x = 11
    rank = 0
    while True:
        digits = [int(i) for i in list(str(x))]
        if sum(digits) == 10:
            rank += 1
            if rank == n:
                return x
        x += 1

print (getPerfectNumber(1))
print (getPerfectNumber(2))
print (getPerfectNumber(3))
print (getPerfectNumber(4))
print (getPerfectNumber(20))
print (getPerfectNumber(100))