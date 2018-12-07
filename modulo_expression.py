#(a * b) % m = ( (a % m) * (b % m) ) % m

#(b ^ -1) % m = (b ^ m-2) % m (Fermat's little theorem)

#( (A mod m) * ( power(B, m-2) % m) ) % m

#Python program without Recursion

A, B = list(map(int,input().strip().split()))

m = 1000000007

def mod(p,q):
    return (p%q)

z = mod(A,m)
w = pow(B,m-2)
s = mod(w,m)
r = mod(z*s,m)

print (r)

