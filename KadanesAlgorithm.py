
ARR = list(map(int,input().strip().split()))

def Kadanes_Algorithm(arr):
    
    max_so_far=max_ending_here=0
    
    for a in range(len(arr)):
        max_ending_here = max_ending_here + arr[a]
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return (max_so_far)

print (Kadanes_Algorithm(ARR))