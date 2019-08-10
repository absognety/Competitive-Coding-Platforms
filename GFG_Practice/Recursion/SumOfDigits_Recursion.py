n = int(input()) 
S = 0             
def recurSum(n,S,L=len(str(n))):
    if L==0:
        print (S)
    else:
        S += n%10
        n = n//10
        recurSum(n,S,L-1)
        
recurSum(n,S)
