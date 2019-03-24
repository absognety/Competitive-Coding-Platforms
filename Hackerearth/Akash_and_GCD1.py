"""
Akash is interested in a new function F such that,

F(x) = GCD(1, x) + GCD(2, x) + ... + GCD(x, x)

where GCD is the Greatest Common Divisor.
Now, the problem is quite simple. Given an array A of size N, there are 2 types of queries:
1. C X Y : Compute the value of F( A[X] ) + F( A[X + 1] ) + F( A[X + 2] ) + .... + F( A[Y] ) (mod 10^9 + 7)
2. U X Y: Update the element of array A[X] = Y

Input:
First line of input contain integer N, size of the array.
Next line contain N space separated integers the elements of A.
Next line contain integer Q, number of queries.
Next Q lines contain one of the two queries.

Output:
For each of the first type of query, output the required sum (mod 10^9 + 7).

Constraints:
1 <= N <= 106
1 <= Q <= 105
1 <= Ai <= 5*105

For Update ,
1 <= X <= N
1 <= Y <= 5*105

For Compute ,
1 <= X <= Y <= N

"""

def GCD(a,b):
    if a == b:
        return (a)
    else:
        minNum = min(a,b)
        maxNum = max(a,b)
        while (minNum!=0):
            maxNum,minNum = minNum,maxNum%minNum
        return (maxNum)

def funcGCD(x):
    sumFunc = 0
    for i in range(1,x+1):
        sumFunc += GCD(i,x)
    return (sumFunc)


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int,input().strip().split()))
    Q = int(input())
    bigInt = (10**9) + 7
    for q in range(Q):
        query = input().strip().split()
        result = 0
        p,q = list(map(int,[query[1],query[2]]))
        if query[0] == 'C':
            s = 0
            while ((p + s) <= q):
                result += funcGCD(arr[p+s-1])
                s += 1
            print (result % bigInt)
        elif query[0] == 'U':
            arr[p-1] = q