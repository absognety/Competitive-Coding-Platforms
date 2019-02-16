n = int(input())
Array = [0]*n
temp=0
for i in range(n):
    Array[i] = int(input())
print (Array)
for k in range(n-1):
    for m in range(n-k-1):
        ##swap case
        if Array[m] > Array[m+1]:
            temp=Array[m]
            Array[m] = Array[m+1]
            Array[m+1]=temp
        m+=1
    k+=1
##Time complexity = O(n**2)