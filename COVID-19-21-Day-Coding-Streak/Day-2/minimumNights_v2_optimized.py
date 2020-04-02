#User function Template for python3

"""
Xenon has A number of sweets , but his lucky number is B . 
Everynight he takes a decision to eat a sweet or not. If he 
chooses to eat , then his number of sweets will get 
decreased by one and if he chooses not to eat , then number 
of sweets gets doubled. Xenon wants to make his number of 
sweets exactly equal to B in minimum number of nights. You 
have to print his optimal decision for Everynight . If he 
eats a sweet at ith night then print "eat" otherwise 
print "overflow" .

Input:
First line of input contains a positive integer T denoting 
number of test cases . For each test case , first line 
contains two space seperated positive integers A (initial number of sweets) 
and B (lucky number) . 

Output:
For each test case , print the sequence of "eat" and "overflow" until 
number of sweets becomes exactly equal to B

Constraints:
1 <= T <= 100
1 <=  A , B <= 10000

Your Task:
This is a funcional problem , you don't need to take input . 
Complete the function getDecision() which accepts two positive integers 
A and B as parameters and returns a vector of strings.

Example:
Input:
2
5 8
1 9
Output:
eat overflow
overflow overflow eat overflow eat overflow eat

Explanation:
Testcase 1: The fastest way to reach 8 from 5 would be 5-4-8 .
Testcase 2: The fastest way to reach 9 from 1 would be 1-2-4-3-6-5-10-9.
"""

def convert(m,n,s):
    if (m==n):
        return 0
    if m > n:
        for i in range(0,m-n):
            s.append("eat")
        return m-n
    if (m <= 0) & (n > 0):
        return -1
    if n%2 == 1:
        s.append("eat")
        return (1 + convert(m,n+1,s))
    else:
        s.append("overflow")
        return (1 + convert(m,n//2,s))

def getDecision(m,n):
    #code here
    ans = []
    convert(m,n,ans)
    return ans


#{ 
#  Driver Code Starts
#Initial Template for Python 3

    
t=int(input())
for _ in range(0,t):
    m,n=list(map(int,input().split()))
    a=getDecision(m,n)
    print(*a[::-1])
            
# } Driver Code Ends