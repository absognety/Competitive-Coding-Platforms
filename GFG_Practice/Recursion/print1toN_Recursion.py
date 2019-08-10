#Initialize i = 1 in v1
def print1toN_v1(n,i):
    if i > n:
        return
    else:
        print (i)
        print1toN_v1(n,i+1)
        
print1toN_v1(24,1)
        
def print1toN_v2(n):
    if n == 0:
        return
    else:
        print1toN_v2(n-1)
        print (n)

print1toN_v2(24)