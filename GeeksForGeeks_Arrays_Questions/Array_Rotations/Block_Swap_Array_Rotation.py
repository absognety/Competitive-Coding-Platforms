arr = list(map(int,input().strip().split()))
n = len(arr)
d = int(input())

def swap(Arr,fi,si,d):
    for i in range(d):
        temp = Arr[fi + i]
        Arr[fi + i] = Arr[si + i]
        Arr[si + i] = temp
        i+=1
    return 

def leftRotate(array, d, n):  
    if(d == 0 or d == n):  
        return
    i = d  
    j = n - d  
    while (i != j):  
          
        if(i < j): # A is shorter 
            swap(array, d - i, d + j - i, i)  
            j -= i          
        else: # B is shorter 
            swap(array, d - i, d, j)  
            i -= j        
    swap(array, d - i, d, i)
    return (array)
    
if __name__ == '__main__':
    print (leftRotate(arr,d,n))
    X = [1,2,3,4,5,6,7]
    print (leftRotate(X,d=2,n=len(X)))
