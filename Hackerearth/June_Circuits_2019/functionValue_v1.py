def recurEven(n):
    if n == 1:
        return (1)
    elif n == 2:
        return (1)
    else:
        return (2*recurEven(n-1) - recurEven(n-2) + 2)

def recurOdd(n):
    if n==1:
        return (1)
    elif n==2:
        return (1)
    else:
        return (3*recurOdd(n-2))
    
def functionValue(L,R,P):
    U = R-L+1
    fvalues = [recurEven(L+i) if (L+i)%2==0 else recurOdd(L+i) for i in range(U)]
    return (sum(fvalues)%P)
    
if __name__ == '__main__':
    T,P = list(map(int,input().strip().split()))
    for _ in range(T):
        L,R = list(map(int,input().strip().split()))
        print (functionValue(L,R,P))