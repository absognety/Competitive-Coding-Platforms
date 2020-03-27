#python3 implementation to find the 
#minimum number of operations in 
#which the array A can be converted 
#to another array B 

# Utility function
def checkArray(arrA,arrB,n):
    operations = 0
    i = 0
    while(i < n):
        # if both elements are equal 
        # move to next element
        if ((arrA[i] - arrB[i])==0):
            i += 1
            continue
        # calculate the difference between
        # two elements
        diff = arrA[i] - arrB[i]
        i += 1
        # loop while next pair of elements have the same 
        # difference
        while ((i < n) & (arrA[i] - arrB[i] == diff)):
            i += 1
        #increase the number of 
        # operations required
        operations += 1
    return operations

# Driver code
if __name__ == '__main__':
    
    a = [3,7,1,4,1,2]
    b = [3,7,3,6,3,2]
    
    c = [1,1,1,1,1]
    d = [1,2,1,3,1]
    
    size1 = len(a)
    size2 = len(c)
    print (checkArray(a,b,size1))
    print (checkArray(c,d,size2))