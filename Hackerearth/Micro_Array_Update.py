def update_array(ARR,k):
    time_array=[]
    for i in range(len(ARR)):
        t=0
        while (ARR[i] < k):
            ARR[i]=ARR[i]+1
            t=t+1
        time_array.append(t)
    return (max(time_array))
        
    
if __name__=='__main__':
    T=int(input())
    for tcase in range(T):
        N,K = list(map(int,input().strip().split()))
        arr = list(map(int,input().strip().split()))
        print (update_array(arr,K))