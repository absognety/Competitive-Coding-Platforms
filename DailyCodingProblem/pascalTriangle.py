"""
Daily Coding Problem: Problem #429

This problem was asked by Stitch Fix.

Pascal's triangle is a triangular array of integers constructed with 
the following formula:

The first row consists of the number 1.
For each subsequent row, each element is the sum of the numbers 
directly above it, on either side.

For example, here are the first few rows:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

Given an input k, return the kth row of Pascal's triangle.

Bonus: Can you do this using only O(k) space?

"""
def binomialCoeff(n,k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        res *= (n-i)
        res = res//(i+1)
    return res

#O(n**3)
def getKthRowOfPascalTriangle(n):
    for line in range(n):
        for i in range(line + 1):
            print (binomialCoeff(line, i),end=" ")
        print ("\n")
        
#O(n**2)
def printPascal(n):
    for line in range(1,n+1):
        C = 1
        for i in range(1,line + 1):
            print (C, end= " ")
            C = C * (line - i)//i
        print ("\n")
        
        
if __name__ == '__main__':
    n = 3
    getKthRowOfPascalTriangle(n)
    printPascal(n)
    n = 7
    getKthRowOfPascalTriangle(n)
    printPascal(n)