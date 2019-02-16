n = int(input())
Array = [0]*n
for i in range(n):
    Array[i] = int(input())
print (Array)

for v in range(n):
    temp = Array[v]
    u = v
    while ((u > 0) & (temp < Array[u-1])):
        Array[u] = Array[u-1]
        u-=1
    Array[u] = temp
    
print (Array)