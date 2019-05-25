import itertools

def printPermutation(N,A):
    numOfElements = pow(2,N)
    bin_reps = []
    for x in range(numOfElements):
        if len(bin(x).split('b')[1]) < 2:
            bin_reps.append(''.join(bin(x).split('b')))
        else:
            bin_reps.append(bin(x).split('b')[1])
    allPerms = list(itertools.permutations(bin_reps,numOfElements))
    total = []
    for xy in allPerms:
        total_sum = []
        for ab in range(len(xy)-1):
            alpha = list(map(int,list(xy[ab])))
            beta = list(map(int,list(xy[ab+1])))
            total_sum.append(sum([abs(alpha[i]-beta[i]) for i in range(len(alpha))]))
        print (total_sum,xy)
        X = list(map(int,list(xy[0])))
        Y = list(map(int,list(xy[len(xy)-1])))
        firstnlastSum = sum([abs(X[i]-Y[i]) for i in range(len(X))])
        if len(bin(A).split('b')[1]) < 2:
            k0 = ''.join(bin(A).split('b'))
        else:
            k0 = bin(A).split('b')[1]
        if (len(set(total_sum))==1) & (list(set(total_sum))[0] == 1) & (firstnlastSum == 1) & (xy[0]==k0) :
            total.append(xy)
    return (total)
    
if __name__ == '__main__':
    N,A = list(map(int,input().strip().split()))
    ans = printPermutation(N,A)
    print (ans)
    for i in ans:
        perm = [int(a,2) for a in i]
        print (perm)