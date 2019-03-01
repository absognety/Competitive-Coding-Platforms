import itertools
arr = list(map(int,input().strip().split()))
n = len(arr)
def sum_arrayInd(array):
    sums=0
    for i,v in enumerate(array):
        sums = sums + (i*v)
    return (sums)
def combination_sums(arr):
    comb_sums=[]
    arr_perms = list(itertools.permutations(arr,len(arr)))
    for x in arr_perms:
        comb_sums.append(sum_arrayInd(x))
    return (max(comb_sums))

if __name__ == '__main__':
    print (combination_sums(arr))