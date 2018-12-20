#Linear Search in indexed interables - Lists, Tuples, Sets

arr = [2,10,8,0,-4,72,37,10,-3,10,2,3,4,8]

x = 8

def linearSearch(arr,x):
    if (arr.count(x)==1):
        return (arr.index(x))
    elif x not in arr:
        print ('Element does not exist')
    elif (arr.count(x)>1):
        inds = [i for i in range(len(arr)) if arr[i]==x]
        return (inds)