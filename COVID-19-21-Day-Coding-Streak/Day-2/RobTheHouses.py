#User function Template for python3

#Complete this function

def kadane(arr,n):
    max_so_far = max_ending_here = 0
    for a in range(n):
        max_ending_here = max_ending_here + arr[a]
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far

def maxMoney(arr,n):
    ##Your code here
    max_kadane = kadane(arr,n)
    max_wrap = 0
    for i in range(n):
        max_wrap += arr[i]
        arr[i] = -1 * arr[i]
    max_wrap = max_wrap + kadane(arr,n)
    if max_wrap > max_kadane:
        return max_wrap
    else:
        return max_kadane

#{ 
#  Driver Code Starts
#Initial Template for Python 3



import math


    
    
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            print(maxMoney(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()


# } Driver Code Ends