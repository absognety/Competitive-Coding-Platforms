arr = list(map(int,input().strip().split()))
n = len(arr)
d = int(input())

def reversal_rotate(arr,m,n):
    A = arr[0:m]
    B = arr[m:n]
    rev_Ar = A[::-1]
    rev_Br = B[::-1]
    ArB = rev_Ar + B
    ArBr = rev_Ar + rev_Br
    BA = ArBr[::-1]
    return(BA)

if __name__ == '__main__':
    print (reversal_rotate(arr,d,n))
    X = [1,2,3,4,5,6,7]
    print (reversal_rotate(X,d,len(X)))