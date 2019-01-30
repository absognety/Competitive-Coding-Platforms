from collections import Counter

arr = list(map(int,input().strip().split()))
Fmax = max(arr)
element_freqs = Counter(arr)
for k,v in element_freqs.items():
    if Fmax%k==0:
        element_freqs[k]-=1

sorted_freqs = sorted(element_freqs.items(),key=lambda x:x[1],
                      reverse=True)
Smax = sorted_freqs[1][0]
print (Fmax,Smax)