"""
BRUTE-FORCE Approach

Given an integer X. Your task is to find out how many positive integers 
N ( 1 <= N <= X)  satisfy the following condition:-


n*(a^n) ≡ b (mod p)


Input:
First line of input contains T denoting the number of test cases. For each 
test case, the first line contains 4 spaces separated integers denoting values 
of  a , b , p and X respectively.

Output:
For each test case, print the number of possible answers  N.

Constraints:
1 <= T <= 100
2 <= p <= 106
1 <= a,b< p
1 <= X <= 1012

Example:
Input:
2
17 17 19 12
2 2 3 19
Output:
1
7

"""

def satisfyTheCondition(a,b,p,X):
    count = 0
    for g in range(1,X+1):
        u = (g*(a**g)) - b
        if u%p == 0:
            count += 1
        else:
            continue
    return count
    
if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        a,b,p,X = list(map(int,input().strip().split()))
        print (satisfyTheCondition(a,b,p,X))
