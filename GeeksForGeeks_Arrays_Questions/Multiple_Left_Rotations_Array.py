arr = list(map(int,input().strip().split()))
n = len(arr)
k1 = int(input())
k2 = int(input())
k3 = int(input())
k4 = int(input())

def initialize(n):
    temp = ['']*(2*n)
    temp[0:n] = arr
    temp[n:] = arr
    return temp

temp = initialize(n)
def LeftRotate(n,k,temp):
    # Starting position of array after k 
    # rotations in temp will be k % n 
    start = k % n 
      
    # Print array after k rotations 
    for i in range(start, start + n): 
        print(temp[i], end = " ") 
    print("") 
    
if __name__ == '__main__':
    LeftRotate(n,k1,temp)
    LeftRotate(n,k2,temp)
    LeftRotate(n,k3,temp)
    LeftRotate(n,k4,temp)