def GCD(a,b):
    if a == b:
        return (a)
    else:
        minNum = min(a,b)
        maxNum = max(a,b)
        while (minNum!=0):
            maxNum,minNum = minNum,maxNum%minNum
        return (maxNum)

def funcGCD(x):
    sumFunc = 0
    for i in range(1,x+1):
        sumFunc += GCD(i,x)
    return (sumFunc)


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int,input().strip().split()))
    Q = int(input())
    bigInt = (10**9) + 7
    for q in range(Q):
        query = input().strip().split()
        result = 0
        p,q = list(map(int,[query[1],query[2]]))
        if query[0] == 'C':
            s = 0
            while ((p + s) <= q):
                result += funcGCD(arr[p+s-1])
                s += 1
            print (result % bigInt)
        elif query[0] == 'U':
            arr[p-1] = q