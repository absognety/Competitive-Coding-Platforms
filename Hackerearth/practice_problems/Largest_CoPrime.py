import math
def largest_coP(n):
    max_coP = 0
    for r in range(1,n-1):
        if math.gcd(r,n) == 1:
            if max_coP < r:
                max_coP = r
    return (max_coP)
        
if __name__ == '__main__':
    n = int(input())
    print (largest_coP(n))