n = int(input())
Array = [0]*n
for i in range(n):
    Array[i] = int(input())
print(Array)

temp = 0
for m in range(n):
    for p in range(m+1,n):
        if Array[m] > Array[p]:
            temp = Array[m]
            Array[m] = Array[p]
            Array[p] = temp
print (Array)

#Time Complexity = O(n**2)