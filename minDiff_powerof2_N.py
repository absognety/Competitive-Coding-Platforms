N = int(input())

import math
def min_diff_N_pow2(N):
    power=math.log(N,2)
    lower_bound = math.floor(power)
    upper_bound = math.ceil(power)
    lower_diff = abs(pow(2,lower_bound)-N)
    upper_diff = abs(pow(2,upper_bound)-N)
    return (min(lower_diff,upper_diff))
    
    
print (min_diff_N_pow2(N))