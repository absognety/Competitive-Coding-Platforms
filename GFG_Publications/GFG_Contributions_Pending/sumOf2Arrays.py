def thirdArray(arrA,arrB,n):
    third_array = [0]*n
    #sort two arrays
    arrA = sorted(arrA)
    arrB = sorted(arrB)
    #Loop to find the array  
    #such that each element is 
    #sum of other two elements 
    for i in range(n):
        third_array[i] = arrA[i] + arrB[i]
    return " ".join(str(q) for q in third_array)


if __name__ == '__main__':
    a = [1,7,8,3]
    b = [6,5,10,2]
    size = len(a)
    print (thirdArray(a,b,size))