def Bit_Even_Arrays(arr):
    for k,v in enumerate(arr):
        z=0
        if v == -1:
            y = k - 1
            z = arr[y]
            while True:
                S = bin(z)[2:][1::2]
                if (z%2==0) & (len(set(S))==1) & ('0' in set(S)):
                    break
                else:
                    z += 1
            arr[k]=z
    return (sum(arr))


if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        N = int(input())
        arr = list(map(int,input().strip().split()))
        print (Bit_Even_Arrays(arr))