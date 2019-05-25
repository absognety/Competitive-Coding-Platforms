# Python 3 arr dynamic programming solution  
# to finding the number of subsets having  
# xor of their elements as k 
import math 
def cumulative_Xor(N,K,A):
    #finding max element of A
    max_element = max(A)
    #maximum possible XOR Value
    m = (1 << (int)(math.log2(max_element) + 1)) - 1
    # The value of dp[i][j] is the number  
    # of subsets having XOR of their elements  
    # as j from the set arr[0...i-1] 
  
    # Initializing all the values  
    # of dp[i][j] as 0 
    dp = [[0 for i in range(m + 1)] for i in range(N + 1)]
    # The xor of empty subset is 0 
    dp[0][0] = 1
  
    # Fill the dp table 
    for i in range(1, N + 1):
        for j in range(m + 1): 
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j ^ A[i - 1]])
    # The answer is the number of subset  
    # from set arr[0..n-1] having XOR of 
    # elements as k
    cnt1 = sum(dp[N][:K])
    cnt2 = dp[N][K]
    cnt3 = sum(dp[N][K+1:])
    return (cnt1,cnt2,cnt3)


if __name__ =='__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        K = int(input())
        A = list(map(int,input().strip().split()))
        ct1,ct2,ct3 = cumulative_Xor(N,K,A)
        print (ct1,ct2,ct3)
        numerator = pow(ct1 + ct2,2) + pow(ct2 + ct3,2) + pow(ct3 + ct1,2) - (ct1**2 + ct2**2 + ct3**2)
        print (numerator%(10**9 + 7))
        