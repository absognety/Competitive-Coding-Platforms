def odd_checker(u):
    binrep = bin(u)[2:]
    checker = [True if i == '0' else False for i in binrep[1::2]]
    if True in checker and False not in checker:
        return (1)
    else:
        return (0)
    
def Bit_Even_Arrays(arr):
    miss_keys = []
    for key,val in enumerate(arr):
        if val == -1:
            miss_keys.append(key)
    for x in miss_keys:
        y = x - 1
        z = arr[y]
        while True:
            if z%2==0 and odd_checker(z)==1:
                break
            else:
                z += 1
        arr[x]=z
    return (sum(arr))


if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        N = int(input())
        arr = list(map(int,input().strip().split()))
        print (Bit_Even_Arrays(arr))
