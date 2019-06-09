def solve (A, R, L):
    # write your code here
    LR_pairs = list(zip(L,R))
    sum_arr = []
    for x,y in LR_pairs:
        myrange = list(range(x-1,y))
        req_arr=[]
        for a in myrange:
            for ind,val in enumerate(A):
                if ((a-ind)%len(A)==0):
                    req_arr.append(val)
                else:
                    continue
        sum_arr.append(sum(req_arr))
    return (sum_arr)
        

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))

    out_ = solve(A, R, L)
    print (' '.join(map(str, out_)))