def flipBits(arr1,arr2):
    bin_arr = arr1
    for q in arr2:
        for i in range(q[0]-1,q[1]):
            if bin_arr[i]==1:
                bin_arr[i]=0
            else:
                bin_arr[i]=1
    return (' '.join(str(i) for i in bin_arr))

if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        N,Q = list(map(int,input().strip().split()))
        arrN = list(map(int,input().strip().split()))
        arr_Q = []
        for q in range(Q):
            arrQ = list(map(int,input().strip().split()))
            arr_Q.append(arrQ)
        print (flipBits(arrN,arr_Q))