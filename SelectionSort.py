n = int(input())
Array = [0]*n
for i in range(n):
    Array[i] = int(input())
print (Array)

temp_minimum=0
TEMP=0
for i in range(n-1):
    temp_minimum=i
    for j in range(i+1,n):
        if Array[j] < Array[temp_minimum]:
            temp_minimum=j
        j+=1
    TEMP=Array[temp_minimum]
    Array[temp_minimum]=Array[i]
    Array[i]=TEMP
    i+=1
print (Array)
#Time Complexity= O(n**2)