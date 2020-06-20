"""
You are given a positive integer N. f(N) is the greatest odd divisor of N. 

Find the sum (f(1)+f(2)+f(3)+f(4)+......f(N))%M.

Input format

The first line of the input contains a single integer T (T <= 100)
denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two integers N and M.

Output format

For each value of N, print the value of (f(1)+f(2)+f(3)+f(4)+......f(N))%M 
in a separate line.

SAMPLE INPUT 
5
1 100
110 30
12345 100000007
10 28383
100 5

SAMPLE OUTPUT 
1
18
50804693
36
4

"""
def greatestOddDivisor(n):
    if n%2 == 1:
        return n
    else:
        while(n%2 == 0):
            n = n//2
    return n

def summoduloM(N,M):
    result = 0
    for u in range(1,N+1):
        result += greatestOddDivisor(u) 
    return (result%M)

if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        N,M = list(map(int,input().strip().split()))
        print (summoduloM(N,M))