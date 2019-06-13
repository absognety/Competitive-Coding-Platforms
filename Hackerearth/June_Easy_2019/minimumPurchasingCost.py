def minimumCost(status_arr,cg,cp,num):
    s1 = 0
    s2 = 0
    for i in status_arr:
        s1 += (i[0]*cg + i[1]*cp)
        s2 += (i[0]*cp + i[1]*cg)
    return (min(s1,s2))


if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        cost_g,cost_p = list(map(int,input().strip().split()))
        num_par = int(input())
        status_arr = []
        for par in range(num_par):
            x,y = list(map(int,input().strip().split()))
            status_arr.append([x,y])
        print (minimumCost(status_arr,cost_g,cost_p,num_par))