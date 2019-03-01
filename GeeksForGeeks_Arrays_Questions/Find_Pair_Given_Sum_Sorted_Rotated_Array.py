import itertools
arr = list(map(int,input().strip().split()))
n = len(arr)
given_sum = int(input())

def findPair(arr,given_sum):
    inds=[]
    for a, b in itertools.combinations(arr,2):
        if a + b == given_sum:
            inds.append('True')
        else:
            inds.append('False')
    if 'True' in inds:
        return ('true')
    else:
        return ('false')
    
if __name__ == '__main__':
    print (findPair(arr,given_sum))